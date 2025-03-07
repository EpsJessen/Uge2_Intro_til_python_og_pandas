import csv
import os.path

fields = []
rows = []
log = []

def read_file(filename:str)->list[str]:
    path = os.path.join("Opgave3", filename)
    dirty_rows = []
    try:
        with open(path, "r") as csv_file:
            csv_reader = csv.reader(csv_file)
            global fields
            fields = (next(csv_reader))

            for row in csv_reader:
                dirty_rows.append(row)
    except OSError:
        log.append(f"ERROR: Could not read file {path}!")
    return dirty_rows

def remove_empty_fields(row:list[str])->list[str]:
    good_entries = []
    for entry in row:
        if entry:
            good_entries.append(entry)
    return good_entries

def clean_rows(dirty_rows:list[str], attempt_cleaning:bool = True, check_content = True):
    number_of_fields = len(fields)
    for number, row in enumerate(dirty_rows, 2):
        # Checks if the number of entries match with the number of fields
        # If not, something is wrong
        if len(row) != number_of_fields:
            # if we want to attempt to clean the data, we check if there has been added too many commas to the entry
            if attempt_cleaning:
                row = remove_empty_fields(row)
                if len(row) != number_of_fields:
                    log.append(f"ERROR: row {number} contains the wrong amount of data!")
                    continue
            # Otherwise we just report the error
            else:
                log.append(f"ERROR: row {number} contains the wrong amount of data!")
                continue

        # Check if there are empty entries
        entry_error = False
        for entry in row:
            if not entry:
                log.append(f"ERROR: row {number} contains empty entries!")
                entry_error = True
                break
        if entry_error:
            continue
        # If no unsolvable problems discovered, add row as clean
        rows.append(row)

def row_to_str(row:list[str])->str:
    data = ""
    for entry in row[:-1]:
        data += entry +","
    data += row[-1]
    return data

def write_file(filename:str)->None:
    path = os.path.join("Opgave3", filename)
    try:
        with open(path, "w") as file:
        
            fields_as_string = row_to_str(fields)
            file.write(fields_as_string + "\n")

            for row in rows:
                data = row_to_str(row)
                file.write(data + "\n")
    except OSError:
        log.append(f"ERROR: could not write to file {path}")

def write_log(path:str)->None:
    try:
        with open(path, "w") as file:
            for line in log:
                file.write(line + "\n")
    except OSError:
        log.append(f"ERROR: could not write log to file {path}")


def main():
    dirty_rows = read_file("source_data.csv")
    clean_rows(dirty_rows, attempt_cleaning=True)
    write_file("cleaned_data.csv")
    logpath = os.path.join("Opgave3", "logfile.txt")
    if log != []:
        print(f"encountered errors during execution, see log @ {logpath}.")
    write_log(logpath)


if __name__ == "__main__":
    main()
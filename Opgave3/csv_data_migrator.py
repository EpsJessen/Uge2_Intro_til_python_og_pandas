import csv
import os.path

fields = []
rows = []

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
        print(f"ERROR: Could not read file {path}!")
    return dirty_rows

def clean_rows(dirty_rows:list[str]):
    number_of_fields = len(fields)
    for number, row in enumerate(dirty_rows, 2):
        if len(row) != number_of_fields:
            print(f"ERROR: row {number} contains the wrong amount of data!")
            continue
        entry_error = False
        for entry in row:
            if not entry:
                print(f"ERROR: row {number} contains empty entries!")
                entry_error = True
                break
        if not entry_error:
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
        print(f"ERROR: could not write to file {path}")
        



def main():
    dirty_rows = read_file("source_data.csv")
    clean_rows(dirty_rows)
    write_file("cleaned_data.csv")

if __name__ == "__main__":
    main()
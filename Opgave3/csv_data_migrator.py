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


def main():
    dirty_rows = read_file("source_data.csv")

if __name__ == "__main__":
    main()
import matplotlib.pyplot as plt
import os.path
import pandas as pd

def import_csv(filename:str="DKHousingPricesSample100k.csv") -> pd.DataFrame:
    path = os.path.join("Opgave4", filename)
    try:
        with open(path, "r") as file:
            df = pd.read_csv(file)
            return df
    except OSError:
        print(f"Could not read file {path}")
    

def main():
    pd.options.display.float_format = '{:.2f}'.format
    
    print("\n\033[31mTask 1:\033[0m")
    df = import_csv()
    print(df.head(10))

    
if __name__ == "__main__":
    main()

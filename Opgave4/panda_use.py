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

    print("\n\033[31mTask 2:\033[0m")
    reg_df = df.groupby("region")[["purchase_price"]].mean()
    print(reg_df)
    reg_df.plot.bar()
    plt.tight_layout()
    plt.show()

    print("\n\033[31mTask 3:\033[0m")
    type_reg_df = df.groupby(["house_type", "region"])[["purchase_price"]].mean()
    unstacked = type_reg_df.unstack()
    a = unstacked.plot(kind="bar", style="plain", title="Prices by location of housing type", ylabel="Price")
    a.legend(labels=["Bornholm", "Fyn & Islands", "Jutland", "Zealand"])
    plt.tight_layout()
    axes = unstacked.plot(kind="bar", subplots=True, layout=(2,2), style="plain", ylabel="Price", legend=False, sharey=True)
    axes[0,0].set_title("Bornholm")
    axes[0,1].set_title("Fyn &\n Islands")
    axes[1,0].set_title("Jutland")
    axes[1,1].set_title("Zealand")
    plt.tight_layout()

    plt.show()
    
    
if __name__ == "__main__":
    main()

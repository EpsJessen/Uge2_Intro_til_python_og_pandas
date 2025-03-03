def get_names() -> None:
    names = []
    try:
        with open("Opgave1/Navne_liste.txt", "r") as file:
            namestext = file.readline()
            names = namestext.split(",")
    except:
        print("Could not read name file")
    return names

def main() -> None:
    list_of_names = get_names()

if __name__ == "__main__":
    main()

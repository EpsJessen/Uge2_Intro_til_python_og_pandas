def get_names() -> None:
    names = []
    try:
        with open("Opgave1/Navne_liste.txt", "r") as file:
            namestext = file.readline()
            names = namestext.split(",")
    except:
        print("Could not read name file")
    return names

def sort_alphabetical(names:list[str])-> list[str]:
    return sorted(names)

def sort_length(names:list[str])->list[str]:
    return sorted(names, key=len)
    
def print_first_n(names:list[str], number:int) -> None:
    for i in range(min(number, len(names))):
        print(names[i])        

def main() -> None:
    list_of_names = get_names()

    alph_sorted = sort_alphabetical(list_of_names)
    print_first_n(alph_sorted, 10)

    len_sorted = sort_length(alph_sorted)
    print_first_n(len_sorted, 10)
if __name__ == "__main__":
    main()

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
    
def dict_letters(names:list[str], case_difference:bool = False) -> dict[str, int]:
    letters = {}
    for name in names:
        if not case_difference:
            name = name.lower()
        for letter in name:
            letters[letter] = letters.get(letter, 0) + 1
    return letters

def print_letter_dict(letter_dict:dict[str, int]) -> None:
    counts_list = letter_dict.items()
    sorted_counts = sorted(counts_list)
    for count in sorted_counts:
        print(f"{count[0]} -> {count[1]}")

def print_first_n(names:list[str], number:int) -> None:
    for i in range(min(number, len(names))):
        print(names[i])        

def main() -> None:
    list_of_names = get_names()

    alph_sorted = sort_alphabetical(list_of_names)
    print_first_n(alph_sorted, 10)

    len_sorted = sort_length(alph_sorted)
    print_first_n(len_sorted, 10)

    name_dict = dict_letters(len_sorted, case_difference=False)
    print_letter_dict(name_dict)


if __name__ == "__main__":
    main()

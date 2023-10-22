# question no 1.......................

def get_season(month):
    seasons = ("winter", "spring", "summer", "autumn")
    if month in [12, 1, 2]:
        return seasons[0]  # Winter
    elif month in [3, 4, 5]:
        return seasons[1]  # Spring
    elif month in [6, 7, 8]:
        return seasons[2]  # Summer
    elif month in [9, 10, 11]:
        return seasons[3]  # Autumn
    else:
        return "Invalid month"

def main():
    while True:
        try:
            month = int(input("Enter a month (1-12) or a negative number to quit: "))
            if month < 0:
                break
            if 1 <= month <= 12:
                season = get_season(month)
                print(f"The season for month {month} is {season}.")
            else:
                print("Invalid input. Please enter a valid month (1-12).")
        except ValueError:
            print("Invalid input. Please enter a valid numeric value.")

if __name__ == "__main__":
    main()


# question no.2......................................
def main():
    names_set = set()

    while True:
        name = input("Enter a name (or press Enter to finish): ")

        if name == "":
            break

        if name in names_set:
            print("Existing name")
        else:
            print("New name")
            names_set.add(name)

    print("\nList of input names:")
    for name in names_set:
        print(name)

if __name__ == "__main__":
    main()


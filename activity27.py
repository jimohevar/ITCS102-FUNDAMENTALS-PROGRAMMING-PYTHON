print("Adding Data to dictionary")
print(" =============================== ")
tuloy = True

empty_dictionary = {}

def print_anime():
    for i,j in empty_dictionary.items():
        print(f"CODE {i} | TITLE -- {j}")

def pang_search(key):
    print("Searching ..... ")
    print(f" result shows {empty_dictionary[key]} on our database") 

while tuloy == True:
    keys = input("Input keys for this anime ---> ")

    value = input("Enter anime title ---> ")


    # adding data to a dictionary
    empty_dictionary[keys] = value

    choice = input("Would you like to continue adding anime \ny-YES\nn-NO\np-PRINT\ns-SEARCH--->  ").lower()

    if choice == 'y':
        print("Continuing.... ")
        continue
    elif choice == 'n':
        print("Program Stops")
        break
    elif choice == 'p':
        print_anime()
        continue
    elif choice == 's':
        code = input("Please input the code of the anime: ")
        pang_search(code)
    else:
        print("Invalid Choice!")
        continue
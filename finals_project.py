
import activity_menu
import code_menu

def main_menu():
    while True:
        name = input("What is your name .?")
        print ("Welcome to my Compiler!", name)
       
        print("\n================= WELCOME TO MY COMPILER =================")
        print("1. Activities")
        print("2. Code Challenges")
        print("3. Exit")

        choice = input("Choose: ")

        if choice == "1":
            activity_menu.show_activity_menu()
        elif choice == "2":
            code_menu.show_code_menu()
        elif choice == "3":
            print("This Program has ended.")
            break
        else:
            print("Invalid choice.")

main_menu()



def show_code_menu():
    while True:
        print("\n=== CODE CHALLENGE LIST ===")
        for i in range(1, 17):
            print(f"{i}. Challenge {i}")
        print("0. Back to Main Menu")

        choice = input("Select challenge: ")

        if choice == "0":
            return
        elif choice == "1":
            import code_challenge1
        elif choice == "2":
            import code_challenge2
        elif choice == "3":
            import code_challenge3
        elif choice == "4":
            import code_challenge4
        elif choice == "5":
            import code_challenge5
        elif choice == "6":
            import code_challenge6
        elif choice == "7":
            import code_challenge7
        elif choice == "8":
            import code_challenge8
        elif choice == "9":
            import code_challenge9
        elif choice == "10":
            import code_challenge10
        elif choice == "11":
            import code_challenge11
        elif choice == "12":
            import code_challenge12
        elif choice == "13":
            import code_challenge13
        elif choice == "14":
            import code_challenge14
        elif choice == "15":
            import code_challenge15
        elif choice == "16":
            import code_challenge16
        else:
            print("Invalid choice.")

        input("\nPress Enter to go back to Challenge List...")

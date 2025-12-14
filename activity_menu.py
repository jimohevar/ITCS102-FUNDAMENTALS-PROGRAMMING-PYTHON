

def show_activity_menu():
    while True:
        print("\n=== ACTIVITY LIST ===")
        for i in range(1, 29):
            print(f"{i}. Activity {i}")
        print("0. Back to Main Menu")

        choice = input("Select activity: ")

        if choice == "0":
            return
        elif choice == "1":
            import activity1
        elif choice == "2":
            import activity2
        elif choice == "3":
            import activity3
        elif choice == "4":
            import activity4
        elif choice == "5":
            import activity5
        elif choice == "6":
            import activity6
        elif choice == "7":
            import activity7
        elif choice == "8":
            import activity8
        elif choice == "9":
            import activity9
        elif choice == "10":
            import activity10
        elif choice == "11":
            import activity11
        elif choice == "12":
            import activity12
        elif choice == "13":
            import activity13
        elif choice == "14":
            import activity14
        elif choice == "15":
            import activity15
        elif choice == "16":
            import activity16
        elif choice == "17":
            import activity17
        elif choice == "18":
            import activity18
        elif choice == "19":
            import activity19
        elif choice == "20":
            import activity20
        elif choice == "21":
            import activity21
        elif choice == "22":
            import activity22
        elif choice == "23":
            import activity23
        elif choice == "24":
            import activity24
        elif choice == "25":
            import activity25
        elif choice == "26":
            import activity26
        elif choice == "27":
            import activity27
        elif choice == "28":
            import activity28
        else:
            print("Invalid choice.")

        input("\nPress Enter to go back to Activity List...")

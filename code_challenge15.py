name = input("Please Enter your Name Before you Start listing your Anime Title : ")
print("Welcome to the List of Anime Titles,", name)
print("List of Anime Titles")

anime_list = []

while True:
    anime = input("Enter the Tiltle of the Anime (or type 'exit' tp finish): ")

    if anime.lower() == 'exit':  # check first before adding
        print("\nAll done! You have exited the anime entry program.")
        print("Your anime list includes:")
        for a in anime_list:
            print(f"- {a}")
        break
    else:
        anime_list.append(anime)
        print("Anime added to the list!")
print(f"\nAll Anime in your list: {anime_list}")

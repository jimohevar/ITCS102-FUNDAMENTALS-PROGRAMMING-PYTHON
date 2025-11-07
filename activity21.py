isClean = True

while isClean == True:
    ask = input("Are the clothes clean already? (Y/N) --> ").lower()
    
    if ask == "y":
        print("Loop continues...")
        continue
    else:
        print("Loop stops.")
        break
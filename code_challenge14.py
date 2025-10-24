identity = input("Whats your name: ")

odd = 0
numb = ""
ft = True

while ft == True:
    num = eval(input("Put a number: "))
    if num % 2 == 1:
        print("Odd Detected")
        odd += num
        numb += str(num) + "," #Will add coma each number until the user decided to stop
        continue
    elif num == 0: #While loop will stop if user input 0
        print("Bye Bye")
        break
    else:
        print("Even spotted")
        print("NOT INCLUDED IN THE SUMMARY")
        continue
print(f"Total of all odd number: {odd}")
print(f"All odd number: {numb}")
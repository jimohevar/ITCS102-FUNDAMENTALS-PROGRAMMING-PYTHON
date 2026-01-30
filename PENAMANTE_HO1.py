
word = input("Enter the word:")

word_length = len(word)

numbers = []

for i in range(word_length):
    num = int(input(f"Enter the number {i+1}:"))
    numbers.append(num)

average = sum(numbers) / len(numbers)

print(f"The length of the word that you typed is {word_length}.")
print(f"The average of the list is {average}.")

if word_length > average:
    print(f"The length of the word that you typed '{word}' is greater than the average {average}.")
elif word_length < average:
    print(f"The length of the word that you typed '{word}' is less than the average {average}.")
else:
    print(f"The length of the word that you typed '{word}' is equal to the average {average}.")
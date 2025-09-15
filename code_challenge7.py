odd_sum = 0 

for i in range(10):
    num = int(input("Enter a number --> :"))
    if num % 2 !=0:
        odd_sum += num
print("The sum off the odd numbers", odd_sum)

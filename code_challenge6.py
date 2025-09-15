num = eval(input("Input a number -->"))

result = 1 

for u in range(num, 0, -1):

     result *= u

print("Factorial is ",result)
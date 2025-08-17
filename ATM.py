
amount = int(input("Enter withdrawal amount (₱): "))

thousands = amount // 1000
amount %= 1000

five_hundreds = amount // 500
amount %= 500

two_hundreds = amount // 200
amount %= 200

hundreds = amount // 100
amount %= 100

fifties = amount // 50
amount %= 50

twenties = amount // 20
amount %= 20

tens = amount // 10
amount %= 10

fives = amount // 5
amount %= 5

ones = amount

print("\n=== Bill Breakdown (Philippine Peso) ===")
print(f"₱1000 bills : {thousands}")
print(f"₱500 bills  : {five_hundreds}")
print(f"₱200 bills  : {two_hundreds}")
print(f"₱100 bills  : {hundreds}")
print(f"₱50 bills   : {fifties}")
print(f"₱20 bills   : {twenties}")
print(f"₱10 coins   : {tens}")
print(f"₱5 coins    : {fives}")
print(f"₱1 coins    : {ones}")
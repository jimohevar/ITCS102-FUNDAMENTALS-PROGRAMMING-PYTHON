def greeter(name):
    print(f"Hi {name}, kamusta ka na ? ")
def summation(x):
    sum = 0 
    for y in range(x, 0, -1):
        sum += y
    print(f"The sum of {x} is {sum}")

summation(11)
summation(7)
summation(2006)
greeter("Jimoh")
greeter("Evar")
greeter("Penamante")
for i in range(2, 6, 1):
    for space1 in range(0, 7):
        print(" ", end=" ")
    for space2 in range(6, i, -1):
        print(" ", end=" ")
    for left in range(3, i):
        print("^", end=" ")
    for right in range(2, i, 1):
        print("^", end=" ")
    print()

for j in range(1, 3, 1):
    for space3 in range(0, 7):
        print(" ", end=" ")
    for space4 in range(-1, j, 1):
        print(" ", end=" ")
    for left2 in range(2, j, -1):
        print("^", end=" ")
    for right2 in range(3, j, -1):
        print("^", end=" ")
    print()

for k in range(2, 9, 1):
    for space5 in range(12, k, -1):
        print(" ", end=" ")
    for left3 in range(2, k, 1):
        print("^", end=" ")
    for right3 in range(1, k):
        print("^", end=" ")
    print()

for m in range(2, 10, 1):
    for space6 in range(12, m, -1):
        print(" ", end=" ")
    for left4 in range(1, m):
        print("^", end=" ")
    for right4 in range(2, m):
        print("^", end=" ")
    print()

for n in range(2, 13, 1):
    for space7 in range(12, n, -1):
        print(" ", end=" ")
    for left5 in range(1, n):
        print("^", end=" ")
    for right5 in range(2, n):
        print("^", end=" ")
    print()

for base_row in range(1, 7):
    for base_space in range(1, 9):
        print(" ", end=" ")
    for base_col in range(1, 9):
        print("^", end="")
    print()

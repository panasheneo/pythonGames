rows = int(input("Enter the number of rows: "))

for i in range(1, rows + 1):
    for j in range(1, rows - i + 1):
        print(end=" ")

    for j in range(1, i + 1):
        print("* ", end="")

    print()
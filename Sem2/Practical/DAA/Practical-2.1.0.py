# Practical 2

# Row Sum

m = int(input("Enter the Number of Row: "))
n = int(input("Enter the number of Columns: "))

matrix = []

for i in range(m):
    data = []
    for j in range(n):
        data.append(int(input("> ")))
    matrix.append(data)

for i in range(m):
    for j in range(n):
        print(matrix[i][j], end="")
    print()

for i in range(m):
    sum = 0
    for j in range(n):
        sum = sum + matrix[i][j]
    print("Sum of Row", i+1, "is", sum)

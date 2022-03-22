# Practical 2.3.0

# Diagonal Sum

def diagonalSum(mat, n):
    principal = 0
    secondary = 0
    for i in range(0, n):
        for j in range(0, n):
            if (i==j):
                principal += mat[i][j]
            if ((i+j)==(n-1)):
                secondary += mat[i][j]
    print("Principal Diagonal Sum:", principal)
    print("Secondary Diagonal Sum:", secondary)

a = [[1, 2, 3, 4],
[5, 6, 7, 8],
[1, 2, 3, 4],
[5, 6, 7, 8]]
n = len(a)

diagonalSum(a, n)

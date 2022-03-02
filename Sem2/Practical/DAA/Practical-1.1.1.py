# Practical 1.1.1

# Printing Sum of Elements in 1D Array
# Without Sum Function

def arrSum(arr):
    total = 0
    for item in arr:
        total+=item
    return total

arr = [1, 2, 3, 4, 5]

n = len(arr)
res = arrSum(arr)

print(arr)
print("Sum of array is", res)
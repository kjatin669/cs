# Practical 1.2.0

def search(arr, n, x):
    for i in range(0, n):
        if (arr[i] == x):
            return i
    return -1

arr = [2, 3, 4, 10, 40]
x = 10
n = len(arr)

result = search(arr, n, x)
print(arr)
if (result == -1):
    print("Element is not present in Array")
else:
    print("Element 10 is present at", result+1, "position")
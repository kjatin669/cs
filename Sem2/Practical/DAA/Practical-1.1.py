# Practical 1.1

# Topic of Practical

def getMin(array, n):
    resMin = array[0]
    for i in range(1, n):
        resMin = min(array[i], resMin)
    return resMin

def getMax(array, n):
    resMax = array[0]
    for i in range(1, n):
        resMax = max(array[i], resMax)
    return resMax

array = [4, 45, 32, 42, 94, 21, 43, 11]
n = len(array)

print(array)
print("The Minimum value of Array is", getMin(array, n))
print("The Maximum Value of Array is", getMax(array, n))

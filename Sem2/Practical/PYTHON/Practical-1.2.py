# Practical 1.2

# Topic of Practical

eleCount = int(input("Enter the Number of Elements: "))

array = []

for i in range(0, eleCount):
    temp = int(input("> "))
    array.append(temp)
    countOdd = 0
    countTemp = 0

for i in range(0, eleCount):
    if (array[i]%2 == 1):
        countOdd = countOdd + 1
    else:
        countEven = countEven + 1

print("Count of Odd Numbers are", countOdd)
print("Count of Even Numbers are", countEven)
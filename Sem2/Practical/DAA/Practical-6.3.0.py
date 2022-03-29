numList = []
number = int(input("Enter the number of elements: "))

for i in range(1, number+1):
    value = int(input("Please Enter Value of %d element: " %i))
    numList.append(value)

numList.sort()

print("Smallest Element:", numList[0])
print("Largest Element:", numList[number-1])

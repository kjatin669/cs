numList = []
number = int(input("Enter the number of elements: "))

for i in range(1, number+1):
    value = int(input("Please Enter Value of %d element: " %i))
    numList.append(value)


smallest = largest = numList[0]

for j in range(1, number):
    if smallest>numList[j]:
        smallest=numList[j]
        min_pos = j
    if largest<numList[j]:
        largest=numList[j]
        max_pos = j

print("Smallest Element in the List:", smallest)
print("Index of Smallest Element:", min_pos)
print("Largest Element in the List:", largest)
print("Index of Largest Element:", max_pos)

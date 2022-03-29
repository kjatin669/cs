numList = []
number = int(input("Enter the number of elements: "))

for i in range(1, number+1):
    value = int(input("Please Enter Value of %d element: " %i))
    numList.append(value)

print("The Smallest Element in the List is", min(numList))
print("The Largest Element in the List is", max(numList))

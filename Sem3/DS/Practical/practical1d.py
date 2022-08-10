A = []

n = int(input('Enter numbers of integers you want to insert in the list: '))
for i in range(0, n):
    x = int(input("Enter Number: "))
    A.append(x)
print(A)

sele = int(input("Enter the Number You Want to Search: "))
if sele in A:
    print("Number Present")
else:
    print("Number not Present")
a = ['Mumbai', 'Banglore', 'Ahmedabad', 'Chandigarh', 'Delhi', 'Pune', 'Jaipur', 'Panji', 'Jodhpur', 'Chennai', 'Hyderabad']

cities = iter(a)
for i in range(0, 10):
    print(next(cities))



a = ['Mumbai', 'Banglore', 'Ahmedabad', 'Chandigarh', 'Delhi', 'Pune', 'Jaipur', 'Panji', 'Jodhpur', 'Chennai', 'Hyderabad']

cities = iter(a)
b = input("Enter the name of City: ")
if b in cities:
    print(b, "is in the list")
else:
    print(b, "is not in the list")



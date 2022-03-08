# Practical No 1

# Write a program code to create console based menu driven program for following file
# 1. Factorial of Number
# 2. Reverse of a Number
# 3. Square Root of a number 
# 4. Summation of n number
# 5. Cube Root of Number
# 6. Palindrome of number
# 7. Armstrong of number
# 8. Summation of factorial number
#7030-6333-2862-6108-653

while 1:
    print("\n(1)Factorial\n(2)Reverse\n(3)Square Root\n(4)Summation of n\n(5)Cube Root\n(6)Palindrome\n(7)Armstong\n(8)Summation\n(9)Exit")
    choice = int(input("Please Select a desired Operation: "))

    if choice == 1:
        fact = 1
        num = float(input("Enter the integer: "))
        while (num>=1):
            fact = fact*num
            num = num-1
        print("The Factorial is", fact)
    elif choice == 2:
        n = input("Enter a Number: ")
        rev = 0
        while (n>0):
            dig = n%10
            n = (rev*10)+dig
            n = n//10
        print("Reverse of number: ", rev)
    elif choice == 3:
        n = float(input("Enter a Number: "))
        sq = n**1/2
        print("The Square root of given Number is", sq)
    elif choice == 4:
        sum = 0
        num = float(input("Enter an Integer: "))
        while (num>=1):
            sum = sum+num
            num = num-1
        print("The Overall Sum is", sum)
    elif choice == 5:
        n = float(input("Enter a Number: "))
        z = n**1/3
        print("The Cube Root of given number is", z)
    elif choice == 6:
        n = int(input("Enter a Number: "))
        temp = n
        rev = 0
        while (n>0):
            dig = n%10
            rev = (rev*10)+dig
            n = n//10
        if (temp==rev):
            print("The Number is Palindrome")
        else:
            print("The Number is Not Palindrome")
    elif choice == 7:
        num = int(input("Enter an Integer: "))
    elif choice == 8:
        f = 1
        s = 0
        n = int(input("Enter the Integer: "))
        for i in range(1, n+1):
            f = f*i
            s = s+f
        print("The Overall Factorised Sum is", s)
    elif choice == 9:
        break
    else:
        print("Invalid Choice, Please choose again")
        print("Thank you for the Interaction")

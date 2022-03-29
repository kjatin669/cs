def jatin_fact(n):
    if n==1:
        return n
    else:
        return n*jatin_fact(n-1)

num=8

if num<0:
    print("The Factorail doesn't exists for Negative Number")
elif num==0:
    print("The Factorial of 0 is 1")
else:
    print("The Factorial of", num, "is", jatin_fact(num))

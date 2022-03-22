class Stack:
    def __init__(self):
        self.items=[]
        self.size=0

    def push(self, value):
        self.items.append(value)
        self.size+=1
    
    def isEmpty(self):
        if(self.size==0):
            return True
        else:
            return False

    def pop(self):
        if self.isEmpty():
            print("Empty")
        else:
            print("The Popped number is", self.items.pop())
            self.size-=1

    def display(self):
        print("Starting from top of elements are")
        self.i = self.size-1
        while self.i>=0:
            print(self.items[self.i])
            self.i-=1

    def peek(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            print("Top Most Element of stack is", self.items[self.size-1])
                
    def length(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            print("Total Elements in the Stack", self.size)


s = Stack()
print("Menu\n1)Push\n2)Pop\n3)Peek\n4)Display\n5)Length\n6)Exit")
choice = int(input("Enter yout Choice: "))
while choice<=5:
    if(choice==1):
        value=int(input("Enter the Number to be Inserted in Stack: "))
        s.push(value)
    elif(choice==2):
        s.pop()
    elif(choice==3):
        s.peek()
    elif(choice==4):
        s.display()
    elif(choice==5):
        s.length()
    choice=int(input("Please Enter Choice:"))

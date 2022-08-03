class List:
    def __init__(self):
        self.list = []
        self.maxSize = 5
        self.size = 0

    def insert(self, value):
        if (self.size == self.maxSize):
            print("List is Full")
        else:
            self.list.append(value)
            self.size+=1
            return self.list

    def remove(self, value):
        if (self.size==0):
            print("List is Empty")
        else:
            self.list.remove(value)
            self.size-=1
            return self.list

    def display(self):
        if (self.size==0):
            print("List is Empty")
        else:
            print(self.list)


class Stack:  
    def __init__(self):
        self.items=[]
        self.size=0
        self.maxSize=5

    def push(self, value):
        if (self.size==self.maxSize):
            print("Stack is Full")
        else:
            self.items.append(value)
            self.size+=1
        
    def pop(self):
        if (self.size==0):
            print("Empty")
        else:
            print("The Popped number is", self.items.pop())
            self.size-=1
    
    def peek(self):
        if (self.size==0):
            print("Stack is Empty")
        else:
            print("Top Most Element of stack is", self.items[self.size-1])
  
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        print("Successfully Enqueue")

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)
        print("Successfully Dequeue")

    def display(self):
        print(self.queue)


myList = List()
myStack = Stack()
myQueue = Queue()

print("""Menu
1) List Insertion
2) List Deletion
3) List Display
4) Stack Push
5) Stack Pop
6) Stack Peek
7) Queue Enqueue
8) Queue Dequeue
9) Queue Display
0) Exit""")

while True:
    choice = int(input("Enter your Choice: "))
    if choice == 1:
        ele = input("Enter Element to be insert: ")
        myList.insert(ele)
        
    elif choice == 2:
        ele = input("Enter Element to be Deleted: ")
        myList.remove(ele)
        
    elif choice == 3:
        myList.display()
        
    elif choice == 4:
        ele = input("Enter Element to be Push: ")
        myStack.push(ele)
        
    elif choice == 5:
        myStack.pop()
        
    elif choice == 6:
        myStack.peek()
        
    elif choice == 7:
        ele = input("Enter Element to be Enqueue: ")
        myQueue.enqueue(ele)
        
    elif choice == 8:
        ele = input("Enter Element to be Dequeue: ")
        myQueue.dequeue(ele)
        
    elif choice == 9:
        myQueue.display()
        
    elif choice == 0:
        break
    
    else:
        print("Incorrect Choice")
    

        

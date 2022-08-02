class List:
    def __init__(self):
        self.list = []
        self.maxSize = 5
        self.size = 0

    def isEmpty(self):
        if (self.size==0):
            return True
        else:
            return False

    def isFull(self):
        if (self.size == self.maxSize):
            return True
        else:
            return False

    def get(self, position):
        return self.list[position]

    def insert(self, value):
        if self.isFull():
            print("List is Full")
        else:
            self.list.append(value)
            self.size+=1
            return self.list

    def insertAt(self, position, value):
        if self.isFull():
            print("List is Full")
        else:
            self.list.insert(position, value)
            self.size+=1
            return self.list

    def remove(self, value):
        if self.isEmpty():
            print("List is Empty")
        else:
            self.list.remove(value)
            self.size-=1
            return self.list

    def removeAt(self, position):
        if self.isEmpty():
            print("List is Empty")
        else:
            self.list.pop(position)
            self.size-=1
            return self.list

    def replace(self, position, value):
        self.list.replace(position, value)
        return self.list

    def size(self):
        return self.size


class Stack:
    def __init__(self):
        self.items=[]
        self.size=0
        self.maxSize=5

    def push(self, value):
        if self.isFull:
            print(|"Stack is Full")
        else:
            self.items.append(value)
            self.size+=1
    
    def isEmpty(self):
        if(self.size==0):
            return True
        else:
            return False

    def isFull(self):
        if(self.size==self.MaxSize):
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


class Queue:
    def __init__(self):
        self.size=0
        self.queue=[]
        self.maxSize = 5

    def enqueue(self, value):
        

    def dequeue(self, value):


    def peek(self):


    def size(self):
        return self.size

    def isEmpty(self):
        if(self.size==0):
            return True
        else:
            return False

    def isFull(self):
        if(self.size==self.MaxSize):
            return True
        else:
            return False


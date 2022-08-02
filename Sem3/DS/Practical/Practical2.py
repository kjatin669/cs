class Node:
    def __init__(self):
        self.data-data
        self.next-None

class LinkedList():
    def _init_(self):
        self.head = None
        self.tail = None
        self.size = 0

    def prepending(self,data):
        newnode = Node(data)
        if self.head == None:
            self.head = newnode
            self.tail = newnode
        else:
            newnode.next = self.head
            self.head = newnode
        print ("newnode inserted at the head position")
        self.size+=1

    def insertfromtail(self,data):
        newnode-Node(data)
        if self.tail==None:
            self.head = newnode
            self.tail = newnode
        else:
            self.tail.next = newnode
            self.tail = newnode
        print ("newnode inserted at the tail position")
        self.size+=1

    def deletefromhead(self):
        if self.head==None:
            print("Linked List empty")
        else:
            value-self head.data
        print("Deleted node is ", value)
        self.head = self.head.next
        self.size-=1

    def deletefromtail(self):
        if self.head==None:
            print("Linked List empty")
        else:
            current=self.head 
            while (current.next!=None):
                prev = current
                current = current.next
            value = current.data
            prev.next = None
            print("Deleted node is ", value)
            self.tail = prev
            self.size-=1

    def traversalofiL(self):
        current= self.head
        while current!=None:
            print (current.data)
            current = current.next
        print ("End")

    def search(self.value):
        self.n = 0
        current-self.head
        while (current!=None):
            self.n+=1
            if current.data-value:
                current-current.next
            else:
                return True
        return False



    def deletevalue(self.value):
        current = self.head
        while (current!-None and current.data!value):
            prev=current
            current=current.next
        if current = None:
            print ("Node not found")
        else:
            self.size-=1
            if current = self.head:
                self.head-current.next
            elif current = self.tail:
                prev.next = current.next
                self.tail = prev
            else:
                prev.next = current.next
            print("value deleted successfully")

x = LinkedList()

print("Menu")
print("1.Prepend \n2.Insert from tail \n3.Delete from head \n4.Delete from tail") print("5.Search for a value \n6.Delete a value \n7.Display Linked List \n8.Exit") choice-int(input("Please enter your choice")) while (choice !-8):
choice = int(input("Enter Your Choice: "))
while(choice!=8)
    if choice == 1:
        value-int(input("enter the value to be inserted"))
        x.prepending(value)
    if choice == 2:
        value-int(input("enter the value to be inserted"))
        x.insertfromtail(value)
    if choice == 3:
        x.deletefromhead()
    if choice == 4:
        x.deletefromtail()
    if choice == 5:
        value=int(input("Enter the value to be searched"))
        result-x.search(value)
        if result == True:
            print ("Value found at node", x.n," in the linked list")
        else:
            print ("Value not found")
    if choice == 6:
        value=int(input("Enter the value to be deleted"))
        x.deletevalue(value)
    if choice == 7:
        x.traversalofLL()
    choice-int(input("Enter ur choice again"))

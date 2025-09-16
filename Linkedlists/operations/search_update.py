class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    
    def traverse(self):
        temp=self.head

        while temp:
            print(temp.data,end=" -> ")
            temp=temp.next
        print("None")


    def search(self,key):
        temp=self.head
        pos=0

        while temp:
            if temp.data==key:
                print(f"found at position {pos}")

            temp=temp.next
            pos+=1
        return print("Not Found")


    def update(self,old,new):
        temp=self.head

        while temp:
            if temp.data==old:
                temp.data=new
                return
            temp=temp.next
        return print("value not found")

ll=LinkedList()
first=Node(10)
second=Node(30)
third=Node(40)

ll.head=first
first.next=second
second.next=third

ll.search(0)

ll.update(30,120)

ll.traverse()
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

ll=LinkedList()
first=Node(10)
second=Node(30)
third=Node(40)

ll.head=first
first.next=second
second.next=third

ll.traverse()
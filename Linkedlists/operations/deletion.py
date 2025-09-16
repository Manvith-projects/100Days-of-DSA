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
#===========================================================    DELETION   =====================================================
    def deletion_at_begining(self):
        if self.head:
            self.head=self.head.next


    def deletion_at_end(self):
        temp=self.head

        if self.head is None:
            return
        
        if self.head.next is None:
            self.head=None

        while temp.next.next:
            temp=temp.next
        temp.next=None

    def deletion_at_position(self, position):
        temp = self.head

        # Case 1: delete head
        if position == 0:
            if temp:
                self.head = temp.next
            else:
                print("List is empty")
            return

        # Traverse to the node before the target
        for _ in range(position - 1):
            if not temp or not temp.next:
                print("Position out of range")
                return
            temp = temp.next

        # If the next node doesn't exist → out of range
        if not temp.next:
            temp.next=None
            return

        # Bypass the target node
        temp.next = temp.next.next


        
    def delete_by_value(self, key):
        if not self.head:
            print("List is empty")
            return
        if self.head.data == key:    # if head is the node to delete
            self.head = self.head.next
            return
        temp = self.head
        while temp.next and temp.next.data != key:
            temp = temp.next
        if temp.next:
            temp.next = temp.next.next
        else:
            print("Value not found")
        

ll=LinkedList()
first=Node(10)
second=Node(30)
third=Node(40)

ll.head=first
first.next=second
second.next=third

# ll.deletion_at_begining()
# ll.deletion_at_end()
ll.deletion_at_position(2)

ll.traverse()
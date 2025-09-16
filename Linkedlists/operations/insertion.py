class Node:
    def __init__(self,data):
        self.data=data            #initailazation of the Linked list.(Structure of linkedlist)
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None           #initailly the linked list has no data

    def traverse(self):
        temp=self.head           #temp is like a pointer here to traverse. it intially starts from first node

        while temp:                        #while the temp or linked list has data in it
            print(temp.data,end=" -> ")    #prints data in linked list
            temp=temp.next                 #moves the temp pointer to the next node
        print("None")
    def insertion_at_head(self,data):
        new_node=Node(data)          #creates a plain new node with next = None
        new_node.next=self.head       # updates the new node pointer to the previous first node
        self.head=new_node          #resets the pointer to the new node as it becomes the first node

    def insertion_at_specific_postion(self,data,position):

        if self.head is None or position==0:     #if there is no data or pos=0 then use the existing method insert at begining
            ll.insertion_at_head(data)
            return

        new_node=Node(data)              #create a new node to insert
        temp=self.head                   #temp is the pointer traverses from the start

        for _ in range(position-1):        # to insert the new node we traverse until we go to our desired postion - 1 to insert

            if not temp:
                print("index out of range !")   #if the postion is not in the linked list. then it is out of range
                return
            temp=temp.next                      #traversing of pointer

        new_node.next=temp.next                #points the new node's next to the node which is orginally in that position. 
                                               #where the new node.next intially is none
        temp.next=new_node              #this is the rewiring of the new node into the linked list. so the pointer can recognize the new node


    def insertion_at_end(self,data):

        new_node=Node(data)
        if not self.head:
            ll.insertion_at_head(data)
            return
        temp=self.head
        while temp.next:
            temp=temp.next

        temp.next=new_node      #has the new node is the end node. we need to update the prev node pointer which is none. to the new node.


ll=LinkedList()
first=Node(10)
second=Node(30)
third=Node(40)

ll.head=first
first.next=second
second.next=third

ll.insertion_at_head(5)
ll.insertion_at_specific_postion(99,3)
ll.insertion_at_end(100)

ll.traverse()
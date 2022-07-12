#Defining the Node Class
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

#Defining the LinkedList class        
#Note : Here the Reversed Linked List is defined inside the LinkedList class.        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert_back(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            temp = self.head
            while temp.next is not None: #iterating to the last element
              temp = temp.next
            temp.next = new_node
            return  
        
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        return
    
    def reverse(self):
        prev = None
        current = self.head #we can directly use head instead of using current pointer
        while current is not None:
            nextptr = current.next
            current.next = prev
            prev = current
            current = nextptr
        self.head = prev #set head to prev after coming out of the loop
        return 




# Driver program to test above functions
llist_a = LinkedList()
llist_a.insert_back(2)
llist_a.insert_back(5)
llist_a.insert_back(6)
llist_a.insert_back(1)
llist_a.print_list()

print('------REVERSED LIST IS----------')
#reverse the linked list
llist_a.reverse()
llist_a.print_list()


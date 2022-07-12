
#to return the middle node of linked list. If there are two middle nodes return the second one

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
    
    #we will find out by using two methods
    #method 1: find count, then find middle element count, iterate and find middle element and return it
    def middle(self):
        count = 0
        temp = self.head
        while temp is not None:
            count = count+1
            temp = temp.next
            
        temp = self.head  
        if temp is None:
            return
                
        middle_node = (count//2)+1
        while middle_node>1:
            temp = temp.next
            middle_node -= 1
        return temp 
    
    #method 2: use two pointers, both pointers point at head initially one pointer increments by one other increments by two
    def middle_pointer(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow
            
 
 
 #driver code to run
llist = LinkedList()
llist.insert_back(2)
llist.insert_back(5)
llist.insert_back(6)
llist.insert_back(1)
llist.insert_back(9)
llist.print_list()

print('Using method 1-----------')
a = llist.middle()
print("The middle element is ", a.value)

print('Using method 2-------------')
b = llist.middle_pointer()
print('The middle element is ',b.value)



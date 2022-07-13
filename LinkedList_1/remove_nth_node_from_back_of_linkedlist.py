#remove nth node from back of linked list


class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        
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
        
    def removeNthFromEnd(self, n):
        if self.head is None:
            return 
        if self.head.next is None and n == 1:
            self.head == None
            return 
        count = 0
        temp = self.head
        while temp is not None:
            count = count + 1
            temp = temp.next
        
        temp = self.head
        node_end = (count - n) + 1
        if node_end == 1:
            temp = temp.next
            self.head = temp
            return
        if node_end == 2:
            temp.next = temp.next.next
            return
        
        while node_end>2:
            node_end = node_end - 1
            temp= temp.next
            
        temp.next = temp.next.next
        return
    
    
 #driver code
llist_a = LinkedList()
llist_a.insert_back(2)
llist_a.insert_back(5)
llist_a.insert_back(6)
llist_a.insert_back(1)
llist_a.print_list()

n = int(input('Enter value of node to remove from end '))
llist_a.removeNthFromEnd(n)

print('-------After removing nth from end-------')
llist_a.print_list()
        

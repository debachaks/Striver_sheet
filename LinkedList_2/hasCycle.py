def hasCycle(self):
    temp = self.head
    if temp is None or temp.next is not None:
        return 
    
    fast = self.head
    slow = self.head
    
    while fast.next is not None and fast.next.next is not None:
        fast = fast.next.next
        slow = slow.next
        if(fast == slow):
            return True

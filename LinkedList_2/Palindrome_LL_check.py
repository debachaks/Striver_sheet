#this solution is optimal in terms of space complexity of O(1)
#solution uploaded in the form of leetcode solution.
class Solution:
    def isPalindrome(self, head) -> bool:
        
        #check if null list or only one element in list
        if head is None or head.next is None:
            return True
        
            
        slow = head
        fast = head
        #find middle node, for even numbered linked list, slow will finally point to first    middle node
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
            
        #helper function inside isPalindrome method
        def reverseList(head):
            prev = None
            nextptr = None
            while head is not None:
                nextptr = head.next
                head.next = prev
                prev = head
                head = nextptr
            return prev
        
        #Reverse the second half
        slow.next = reverseList(slow.next)
        
        #move slow to right half
        slow = slow.next
        
        #check simultaneously if values of first half of linked list and reversed second half is same
        while slow is not None:
            if head.val != slow.val:
                return False
            head = head.next
            slow = slow.next
        return True
    

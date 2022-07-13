#In the format of leetcode solution, optimal approach with time complexity O(2m), m is length of larger linked list, and space complexity O(1)

class Solution:
    def getIntersectionNode(self, headA, headB):
        if headA is None and headB is None:
            return None
        a = headA
        b = headB
        
        while a != b:
            if a is None:
                a = headB
            else:
                a = a.next
            
            if b is None:
                b = headA
            else:
                b = b.next
                
        return a

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        
        def getPath(node,arr,B):
            if node is None:
                return False
            arr.append(node.val)
            if node.val == B:
                return True
            if getPath(node.left,arr,B) or getPath(node.right,arr,B):
                return True
            arr.pop(len(arr)-1)
            return False
        
        arr = []
        if A is None:
            return False
            
        getPath(A,arr,B)

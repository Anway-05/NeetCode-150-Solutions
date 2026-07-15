# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def bst(root,upper,lower):
            if not root:
                return True
            if not (lower<root.val<upper):
                return False
            return bst(root.left,root.val,lower) and bst(root.right,upper,root.val)

        return bst(root,float("inf"),float("-inf"))
            


            
            
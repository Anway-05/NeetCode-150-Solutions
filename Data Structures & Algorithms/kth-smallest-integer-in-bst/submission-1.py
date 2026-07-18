# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.stored=[]
        def inorder(root):
            if not root:
                return None
            inorder(root.left)
            self.stored.append(root.val)
            inorder(root.right)
        inorder(root)
        return self.stored[k-1]
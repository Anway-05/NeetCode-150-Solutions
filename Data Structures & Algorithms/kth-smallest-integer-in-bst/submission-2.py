# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k=k
        def inorder(root):
            if not root:
                return None
            left=inorder(root.left)
            if left!=None:
                return left
            if self.k==1:
                return root.val
            self.k-=1
            right=inorder(root.right)
            if right!=None:
                return right
        return inorder(root)
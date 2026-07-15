# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        self.count=0

        def dfs(node,max_element):
            if not node:
                return 0
            if node.val>=max_element:
                self.count+=1
                max_element=node.val
            dfs(node.left,max_element)
            dfs(node.right,max_element)
        
        dfs(root,float("-inf"))

        return self.count


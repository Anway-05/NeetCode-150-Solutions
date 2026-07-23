# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.stored=[]
        def dfs(root):
            if not root:
                self.stored.append("#")
                return
            self.stored.append(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return ",".join(map(str,self.stored))
            
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = data.split(",")
        self.i=0
        def dfs():
            if data[self.i]=='#':
                self.i+=1
                return None
            node=TreeNode(int(data[self.i]))
            self.i+=1
            node.left=dfs()
            node.right=dfs()
            return node
        return dfs()
            
            








class TrieNode:
    def __init__(self):
        self.children={}
        self.isEnd=False
        self.word=None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root=TrieNode()
        for word in words:
            node=root
            for ch in word:
                if ch not in node.children:
                    node.children[ch]=TrieNode()
                node=node.children[ch]
            node.isEnd=True
            node.word=word
        final_list=[]
        visited=set()
        def dfs(node,i,j):
            if i<0 or j<0 or i>len(board)-1 or j>len(board[0])-1:
                return
            if (i,j) in visited:
                return
            ch=board[i][j]
            if ch not in node.children:
                return
            visited.add((i,j))
            node=node.children[ch]       
            if node.isEnd:
                if node.word not in final_list:
                    final_list.append(node.word)
            dfs(node,i+1,j)
            dfs(node,i-1,j)
            dfs(node,i,j+1)
            dfs(node,i,j-1)
            visited.remove((i,j))
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(root,i,j)
        return final_list
            
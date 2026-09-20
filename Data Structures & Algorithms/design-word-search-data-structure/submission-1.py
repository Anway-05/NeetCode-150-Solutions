class TrieNode:
    def __init__(self):
        self.children={}
        self.isEnd=False

class WordDictionary:

    def __init__(self):
        self.root=TrieNode()

    def addWord(self, word: str) -> None:
        node=self.root
        for ch in word:
            if ch in node.children:
                node=node.children[ch]
            else:
                new_node=TrieNode()
                node.children[ch]=new_node
                node=new_node
        node.isEnd=True

    def search(self, word: str) -> bool:
        def dfs(node,i):
            if i==len(word):
                return node.isEnd
            ch=word[i]
            if ch=='.':
                for child in node.children:
                    if dfs(node.children[child],i+1):
                        return True
                return False
            if ch not in node.children:
                return False
            return dfs(node.children[ch],i+1)
        return dfs(self.root,0)
        

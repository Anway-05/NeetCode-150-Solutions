class TrieNode:
    def __init__(self):
        self.children={}
        self.isEnd=False

class PrefixTree:

    def __init__(self):
        self.root=TrieNode()       

    def insert(self, word: str) -> None:
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
        node=self.root
        for ch in word:
            if ch not in node.children:
                return False
            else:
                node=node.children[ch]
        return node.isEnd

    def startsWith(self, prefix: str) -> bool:
        node=self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            else:
                node=node.children[ch]
        return True
        
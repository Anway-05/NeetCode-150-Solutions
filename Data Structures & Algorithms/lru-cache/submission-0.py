class node:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.prev=None
        self.next=None

class LRUCache:

    def __init__(self, capacity: int):
        self.head=node(0,0)
        self.tail=node(0,0)
        self.head.next=self.tail
        self.tail.prev=self.head
        self.capacity=capacity
        self.lookup={}
    
    def remove(self,node):
        node.prev.next=node.next
        node.next.prev=node.prev

    def insert(self,node):
        node.prev=self.head
        node.next=self.head.next
        self.head.next.prev=node
        self.head.next=node

    def get(self, key: int) -> int:
        if key in self.lookup:
            self.remove(self.lookup[key])
            self.insert(self.lookup[key])
            return self.lookup[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.lookup:
            self.lookup[key].val=value
            self.remove(self.lookup[key])
            self.insert(self.lookup[key])
        else:
            if len(self.lookup)==self.capacity:
                del self.lookup[self.tail.prev.key]
                self.remove(self.tail.prev)
            self.lookup[key]=node(key,value)
            self.insert(self.lookup[key])






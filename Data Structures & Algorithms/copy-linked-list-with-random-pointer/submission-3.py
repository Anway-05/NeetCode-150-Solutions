"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        curr=head
        while curr:
            temp=curr.next
            curr.next=Node(curr.val,temp,None)
            curr=temp
        curr=head
        while curr:
            if curr.random == None:
                curr.next.random=None
            else:
                curr.next.random=curr.random.next
            curr=curr.next.next
        head1=head.next
        main=head
        copy=head1
        while copy and copy.next:
            main.next=main.next.next
            copy.next=copy.next.next
            main=main.next
            copy=copy.next
        main.next=None
        return head1
    
        

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
        lookup={}
        dummy=Node(0)
        copy=dummy
        main=head
        while main:
            copy.next=Node(main.val,None,None)
            copy=copy.next
            lookup[main]=copy
            main=main.next
        head1=dummy.next
        copy=head1
        main=head
        while copy:
            if main.random == None:
                copy.random=None
            else:
                copy.random=lookup[main.random]
            main=main.next
            copy=copy.next
        return head1

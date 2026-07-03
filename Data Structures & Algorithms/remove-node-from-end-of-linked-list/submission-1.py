# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr_n=curr=head
        i=1
        while i<=n:
            i+=1
            curr_n=curr_n.next
        if curr_n==None:
            return head.next
        while curr_n.next:
            curr_n=curr_n.next
            curr=curr.next
        curr.next=curr.next.next
        return head
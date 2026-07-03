# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        curr,prev=head,None
        while curr:
            temp=curr.next
            curr.next=prev
            prev,curr=curr,temp
        head1=prev
        if n==1:
            prev=prev.next
        else:
            i=1
            while i<n-1:
                head1=head1.next
                i+=1
            head1.next=head1.next.next
        head=prev
        curr,prev=head,None
        while curr:
            temp=curr.next
            curr.next=prev
            prev,curr=curr,temp
        return prev




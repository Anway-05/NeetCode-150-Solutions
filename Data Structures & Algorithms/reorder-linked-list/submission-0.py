# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        slow,fast=head,head.next
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        curr,prev=slow.next.next,slow.next
        slow.next=None
        prev.next=None
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        head1=head
        head2=prev
        while head1 and head2:
            temp1=head1.next
            temp2=head2.next
            head1.next=head2
            head2.next=temp1
            head1=temp1
            head2=temp2
        

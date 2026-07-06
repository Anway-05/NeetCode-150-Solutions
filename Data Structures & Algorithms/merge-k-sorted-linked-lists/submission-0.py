# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution: 
    def merge2lists(self,list1,list2):
        dummy=ListNode()
        head1,head2,head3=list1,list2,dummy
        while head1 and head2:
            if head1.val<head2.val:
                head3.next=head1
                head1=head1.next
            else:
                head3.next=head2
                head2=head2.next
            head3=head3.next
        if head1:
            while head1:
                head3.next=head1
                head1=head1.next 
                head3=head3.next
        else:        
            while head2:
                head3.next=head2
                head2=head2.next 
                head3=head3.next
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        final_list1=deque(lists)
        if len(final_list1)<1:
            return None
        while len(final_list1)>1:
            final_list1.append(self.merge2lists(final_list1.popleft(),final_list1.popleft()))
        return final_list1[0]









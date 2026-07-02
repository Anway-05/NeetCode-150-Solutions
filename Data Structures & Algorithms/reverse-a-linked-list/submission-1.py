# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
            if head == None or head.next == None:
                return head
            if head.next.next == None:
                tail=head.next
                head.next=None
                tail.next=head
                return tail
            temp1=head
            temp2=temp1.next
            temp3=temp2.next
            temp1.next=None
            while temp3.next != None:
                temp2.next=temp1
                temp1=temp2
                temp2=temp3
                temp3=temp3.next
            temp2.next=temp1
            temp3.next=temp2
            return temp3
            

            
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1,n2=l1,l2
        dummy=ListNode()
        curr=dummy
        carry=0
        while n1 or n2:
            if n1 and n2:
                value=((n1.val+n2.val+carry)%10)
                curr.next=ListNode(value,None)
                carry=(n1.val+n2.val+carry)//10
                n1,n2,curr=n1.next,n2.next,curr.next
            elif not n1:
                value=(n2.val+carry)%10
                curr.next=ListNode(value,None)
                carry=(n2.val+carry)//10
                n2,curr=n2.next,curr.next
            else:
                value=(n1.val+carry)%10
                curr.next=ListNode(value,None)
                carry=(n1.val+carry)//10
                n1,curr=n1.next,curr.next

        if carry!=0:
            curr.next=ListNode(carry,None)

        return dummy.next


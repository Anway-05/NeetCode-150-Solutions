# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # def return_tail(self,head,k):
    #     count=0
    #     while count!=k:
    #         if head.next==None and count<k-1:
    #             return None
    #         count+=1
    #         head=head.next
    #     return head
    def return_tail(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr=head
        dummy=ListNode(0,curr)
        final_head=self.return_tail(dummy,k)
        if final_head==None:
            return head
        while curr:
            prev=curr
            head_k=curr
            tail=self.return_tail(curr,k)
            if tail == None:
                check = curr
                cnt = 0
                while check and cnt < k:
                    check = check.next
                    cnt += 1
                if cnt < k:
                    break
            curr=curr.next
            while curr!=tail:
                temp=curr.next
                curr.next=prev
                prev=curr
                curr=temp
            dummy1=ListNode(0,curr)
            head_k_next=self.return_tail(dummy1,k)
            if head_k_next==None:
                head_k.next=curr
            else:
                head_k.next=head_k_next
        return final_head






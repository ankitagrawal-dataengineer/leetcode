# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        if not head or left==right:
            return head
        
        t=head
        before=None
        pos=1
        while pos<left:
            before=t
            t=t.next
            pos+=1
            continue
        
        curr=t
        prev=None
        times=right-left+1
        while times>0:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
            times-=1
        t.next=curr
        if before:
            before.next=prev
            return head
        return prev
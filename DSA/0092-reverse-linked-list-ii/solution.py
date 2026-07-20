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
        if not head and left==right:
            return head
        pos,t,before=1,head,None
        while pos<left:
            before=t
            t=t.next
            pos+=1
            continue
        times=right-left+1
        curr,prev=t,None
        while times:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
            times-=1
        t.next=curr
        if before:
            before.next=prev
            return head
        return prev
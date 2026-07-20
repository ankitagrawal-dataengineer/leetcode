# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head:
            return head
        last=head
        n=1
        while last.next:
            n+=1
            last=last.next
        k=k%n
        if k==0:
            return head
        count=1
        t=head
        c=n-k

        while count<c:
            count+=1
            t=t.next
        last.next=head
        res=t.next
        t.next=None
        return res

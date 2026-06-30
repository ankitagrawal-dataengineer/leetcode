# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return head
        off=head
        cm=head.next
        while cm:
            if cm.val==off.val:
                cm=cm.next
            else:
                off.next=cm
                off=off.next
                cm=cm.next
        off.next=None
        return head

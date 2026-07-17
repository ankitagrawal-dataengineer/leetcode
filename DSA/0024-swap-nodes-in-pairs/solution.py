class Solution(object):

    def reverse(self,head,times):
        curr=head
        prev=None
        while times>0:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
            times-=1
    
    # prev = new head
    # head = new tail
    # curr = next group's first node

    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return head

        left=head
        prev_left=res=None
        size=2

        while True:
            right=left
            for i in range(size-1):
                if not right:
                    break
                right=right.next
            if right:
                next_left=right.next
                self.reverse(left,size)
                if prev_left:
                    prev_left.next=right
                prev_left=left
                if res==None:
                    res=right
                left=next_left
            else:
                if prev_left:
                    prev_left.next=left
                elif res==None:
                    res=left
                break
        return res
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

    def reverseKGroup(self, head, k):
        if not head:
            return head

        left=head
        prev_left=res=None

        while True:
            right=left
            for i in range(k-1):
                if not right:
                    break
                right=right.next
            if right:
                next_left=right.next
                self.reverse(left,k)
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
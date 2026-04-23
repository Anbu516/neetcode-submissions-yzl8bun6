# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        dummy = ListNode()
        dummy.next = head

        gprv = dummy

        while True:
            kth = self.getKth(gprv,k)
            if not kth:
                break
            gnext = kth.next

            prv,cur = kth.next,gprv.next

            while cur!=gnext:
                temp = cur
                cur = cur.next
                temp.next = prv
                prv = temp
            
            temp = gprv.next
            gprv.next = kth
            gprv = temp
        
        return dummy.next

    def getKth(self,curr,k):
        while curr and k>0:
            curr = curr.next
            k -= 1
        return curr
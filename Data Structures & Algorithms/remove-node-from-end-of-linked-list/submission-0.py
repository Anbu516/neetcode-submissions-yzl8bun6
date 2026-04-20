# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        n1 = 0
        temp = head
        while temp:
            n1+=1
            temp = temp.next
        if n==n1:
            return head.next
        n = n1-n
        c = 0
        temp = head
        while temp:
            if c == n and n!=0:
                prv.next = temp.next
                temp.next = None
            prv=temp
            temp=temp.next
            c+=1
        return head
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        temp = slow
        while fast and fast.next:
            temp =slow
            slow = slow.next
            fast=fast.next.next

        l2 = slow.next
        prv = slow.next = None

        while l2:
            temp = l2
            l2 = l2.next
            temp.next = prv
            prv = temp
        
        l1,l2 = head,prv

        while l2:
            temp1,temp2=l1.next,l2.next
            l1.next = l2
            l2.next = temp1
            l1,l2 = temp1,temp2
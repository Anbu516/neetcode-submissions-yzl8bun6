# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p=list1
        q=list2
        s=ListNode()
        if p==None: return q
        if q==None: return p

        if p.val<=q.val:
            s=p
            p=p.next
        else:
            s=q
            q=q.next
        temp=s
        while p!=None and q!=None:
            if p.val<=q.val:
                temp.next=p
                p=p.next
            else:
                temp.next=q
                q=q.next
            temp=temp.next
        while p!=None:
            temp.next=p
            p=p.next
            temp=temp.next
        while q!=None:
            temp.next=q
            q=q.next
            temp=temp.next
        return s
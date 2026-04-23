# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def merge(l1,l2):

            if not l1:
                return l2

            if not l2:
                return l1
            
            s = ListNode()

            if l1.val<=l2.val:
                s = l1
                l1 = l1.next
            
            else:
                s = l2
                l2 = l2.next
            
            temp = s
            while l1 and l2:
                if l1.val<=l2.val:
                    temp.next = l1
                    l1 = l1.next
                else:
                    temp.next = l2
                    l2 = l2.next
                temp = temp.next
            
            while l1:
                temp.next = l1
                l1 = l1.next
                temp = temp.next
            
            while l2:
                temp.next = l2
                l2 = l2.next
                temp = temp.next
            
            return s

        if len(lists) == 0:
            return None

        if len(lists) == 1:
            return lists[0]
        
        l1 = lists[0]
        
        for i in range(1,len(lists)):
            l2 = lists[i]
            l1 = merge(l1,l2)
        
        return l1
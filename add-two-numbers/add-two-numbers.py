# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = 0 
        head = nxt = ListNode()
        
        while l1 or l2 or res:
            if l1:
                res += l1.val
                l1 = l1.next
            if l2:
                res += l2.val
                l2 = l2.next
            
            res, val = divmod(res, 10)
            nxt.next = nxt = ListNode(val)
            
            print(nxt)
            
        return head.next
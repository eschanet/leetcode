# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        result_list = []
        while l1 and l2:
            if l1.val <= l2.val:
                result_list.append(l1.val)
                l1 = l1.next
            else:
                result_list.append(l2.val)
                l2 = l2.next
       
        l = l1 if l1 else l2
        while l:
            result_list.append(l.val)
            l = l.next
        
        if not result_list: return ListNode().next # this feels dirty
        
        result_listnode = ListNode(result_list[0])
        tail = result_listnode
        
        i = 1
        while i < len(result_list):
            tail.next = ListNode(result_list[i])
            tail = tail.next
            i += 1
            
        return result_listnode
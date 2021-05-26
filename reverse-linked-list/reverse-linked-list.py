# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution: 
    def recursive_reverse(self, head: ListNode, previous = None) -> ListNode:
        tail = head.next
        head.next = previous
        if tail:
            return self.recursive_reverse(tail, head)
        else:
            return head
            
    def iterative_reverse(self, head: ListNode) -> ListNode:
        previous = None
        current = head
        following = head.next
        
        while current:
            current.next = previous
            previous = current
            current = following
            if following:
                following = following.next
        
        return previous
        
    def reverseList(self, head: ListNode) -> ListNode:
        if not head: return ListNode().next
        
        # return self.recursive_reverse(head)
        return self.iterative_reverse(head)

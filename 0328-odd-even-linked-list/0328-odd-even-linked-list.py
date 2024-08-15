# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        
        odd=head
        even=head.next
        evenhead=even
        
        while even and even.next:
            odd.next=odd.next.next
            odd=odd.next
            
            even.next = even.next.next
            even= even.next
        
        odd.next=evenhead
        
        return head
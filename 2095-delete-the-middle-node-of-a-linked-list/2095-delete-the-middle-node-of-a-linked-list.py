# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        slow,fast=head,head
        if not head or not head.next :
            return None
        
        while fast.next.next and fast.next.next.next:
            slow=slow.next
            fast=fast.next.next
            
        slow.next=slow.next.next
        return head
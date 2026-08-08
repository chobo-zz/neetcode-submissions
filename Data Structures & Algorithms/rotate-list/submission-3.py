# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        dummy = head
        length = 1
        while dummy.next:
            dummy = dummy.next
            length += 1
        
        dummy2 = head
        k = k % length
        if not k:
            return head
        
        for i in range(length - k - 1):
            dummy2 = dummy2.next
        
        newHead = dummy2.next
        dummy2.next = None
        dummy.next = head
        head = newHead
        return head
        
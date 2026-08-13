# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        # get node right before left pointer

        before = dummy
        for _ in range(left - 1):
            before = before.next

        cur = before.next

        # reverse starting at cur up to right pointer
        prev = before
        for _ in range(right - left + 1):
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        # cur now pointing at the node right after reversed list

        before.next.next = cur
        before.next = prev

        return dummy.next
        
        
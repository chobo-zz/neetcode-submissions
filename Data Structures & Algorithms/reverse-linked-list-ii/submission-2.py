# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        cur = dummy
        # get node 1 before left pointer
        for i in range(left - 1):
            cur = cur.next
        
        beforeLeft = cur

        # reverse list up to right pointer
        prev = None
        cur = beforeLeft.next
        for i in range(right - left + 1):
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        afterRight = cur

        tmp = beforeLeft.next
        beforeLeft.next = prev
        tmp.next = cur

        return dummy.next
        
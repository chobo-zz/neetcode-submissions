# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return head

        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse second half of list
        second = slow.next
        slow.next = None # break the link of first half
        prev = None

        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merge two lists
        first, second = head, prev
        while second: # we choose second since it could be shorter list (odd length list)
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
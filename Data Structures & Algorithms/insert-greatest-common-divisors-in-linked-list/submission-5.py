# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        cur = dummy

        while cur.next and cur.next.next:
            first = cur.next
            second = cur.next.next
            newNode = ListNode(math.gcd(first.val, second.val))
            first.next = newNode
            newNode.next = second
            cur = cur.next.next
        return dummy.next

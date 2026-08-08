# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head

        while cur.next:
            tmp = cur.next

            gcd = math.gcd(cur.val, cur.next.val)
            cur.next = ListNode(gcd)
            cur.next.next = tmp

            cur = cur.next.next
        
        return head


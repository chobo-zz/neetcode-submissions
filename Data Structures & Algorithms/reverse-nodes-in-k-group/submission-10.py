# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prevGroup = dummy

        while True:
            kth = self.getKthNode(prevGroup, k)
            if not kth:
                break

            # reverse current k-group
            curr = prevGroup.next
            prev = nextGroup = kth.next
            while curr != nextGroup:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            # reconnect pointers
            temp = prevGroup.next
            prevGroup.next = kth
            prevGroup = temp

        return dummy.next
    
    def getKthNode(self, node, k):
        while node and k:
            node = node.next
            k -= 1
        return node
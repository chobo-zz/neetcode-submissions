# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        
        dummy = prevGroup = ListNode(0, head)
        
        while True:
            kth = self.getKth(prevGroup, k)

            if not kth:
                break
            
            prev = nextGroup = kth.next
            curr = prevGroup.next

            while curr != nextGroup:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            temp = prevGroup.next
            prevGroup.next = kth
            prevGroup = temp
        
        return dummy.next



        
    
    def getKth(self, node, k):
        while node and k > 0:
            node = node.next
            k -= 1
        return node
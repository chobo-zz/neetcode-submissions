# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find second half of list
        # reverse it
        # then merge first and second 
        # second half may be shorter if odd, so use that for the while condition

        if not head:
            return
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None # break link between first and second half

        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        # now merge first and second
        first = head
        second = prev
        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
            



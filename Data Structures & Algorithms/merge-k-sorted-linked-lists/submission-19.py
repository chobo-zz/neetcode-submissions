# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # divide and conquer: merge two lists at a time

        if not len(lists):
            return None

        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i + 1] if (i + 1) < len(lists) else None

                mergedList = self.mergeLists(list1, list2)
                mergedLists.append(mergedList)
            lists = mergedLists
        
        return lists[0]
    
    def mergeLists(self, list1, list2):
        dummy = head = ListNode(0)
        while list1 and list2:
            if list1.val < list2.val:
                dummy.next = ListNode(list1.val)
                list1 = list1.next
            else:
                dummy.next = ListNode(list2.val)
                list2 = list2.next
            dummy = dummy.next
        dummy.next = list1 or list2
        return head.next

        
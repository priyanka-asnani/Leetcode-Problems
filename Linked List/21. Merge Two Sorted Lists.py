# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        # edge case
        if not list1:
            return list2
        if not list2:
            return list1
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
            # gather the remaining elements in l1 and l2
            if list1:
                curr.next = list1
            elif list2:
                curr.next = list2
        return dummy.next
    
## Time Complexity: O(N)
## Space Complexity: O(1)
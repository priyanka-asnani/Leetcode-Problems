# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        hashset = set(nums)
        count = 0
        curr = head
        connected = False
        # iterate over the list
        while curr:
            if curr.val in hashset and not connected:
                connected = True
                count += 1
            elif curr.val not in hashset and connected:
                connected = False
            curr = curr.next
        return count
    
## Time Complexity: O(N)
## Space Complexity: O(N)
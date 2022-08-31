class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left, max_len = 0, 0
        hashmap = {}
        for right in range(len(fruits)):
            if fruits[right] not in hashmap:
                hashmap[fruits[right]] = 0
            hashmap[fruits[right]] += 1
            fruits_length = right - left + 1
            if len(hashmap) <= 2:
                max_len = max(fruits_length, max_len)
            
            # if length hashamap exceeds two
            if len(hashmap) > 2:
                # decrement the value of the element at the left pointer
                left_fruit = fruits[left]
                hashmap[left_fruit] -= 1
                if hashmap[left_fruit] == 0:
                    del hashmap[left_fruit]
                # slide the window
                left += 1
        return max_len
    
## Time Complexity: O(N)
## Space Complexity: O(1)
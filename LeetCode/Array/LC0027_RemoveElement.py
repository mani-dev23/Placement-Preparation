"""
LeetCode #27 - Remove Element

Approach:
- Two Pointers (Slow & Fast)

Time Complexity: O(n)
Space Complexity: O(1)
"""


nums = [3,2,2,3]
val = 3


class Solution(object):
    def removeElement(self, nums, val):
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
        return slow

sol = Solution()
print(sol.removeElement(nums, val))


# Time Complexity: O(n)
# Space Complexity: O(1)
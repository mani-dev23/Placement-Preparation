"""
LeetCode #26 - Remove Duplicates from Sorted Array

Approach:
- Two Pointers (Slow & Fast)

Time Complexity: O(n)
Space Complexity: O(1)
"""




class Solution(object):
    def removeDuplicates(self, nums):

        slow = 0
        for fast in range(1, len(nums)):

            if nums[slow] != nums[fast]:
                slow +=1
                nums[slow] = nums[fast]
        return slow + 1 

sol = Solution()

print(sol.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
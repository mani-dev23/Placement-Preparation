"""
LeetCode #217 - Contains Duplicate

Approach:
- Hash Set

Time Complexity: O(n)
Space Complexity: O(n)
"""  




nums = [1,2,3,1]


class Solution(object):
    def ContainsDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)    
        return False
    
sol = Solution()

print(sol.ContainsDuplicate(nums))

# Time Complexity O(n)
# Space Complexity O(n)

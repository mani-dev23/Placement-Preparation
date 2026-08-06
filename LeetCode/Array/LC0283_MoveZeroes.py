nums = [0, 1, 0, 3, 12]


class Solution(object):
    def moveZeroes(self, nums):
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[fast], nums[slow] = nums[slow], nums[fast]
                slow +=1
        return nums

    
sol= Solution()
print(sol.moveZeroes(nums))

# Time complexity O(n)
# Space Complexity O(1)
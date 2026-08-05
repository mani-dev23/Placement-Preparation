nums = [1,2,3,1]


def dupliate(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False

print(dupliate(nums))

# Time Complexity O(n**2)
# Space Complexity O(1)


def containsDuplicate(nums):
    nums.sort()   # Sort the array

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return True

    return False

# Time Complexity O(n log n)
# Space Complexity O(1)


class Solution(object):
    def containsDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)    
        return False
    
sol = Solution()

print(sol.containsDuplicate(nums))

# Time Complexity O(n)
# Space Complexity O(n)

set = set()
set.add(5)
print(set)



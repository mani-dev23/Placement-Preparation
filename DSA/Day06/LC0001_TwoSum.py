"""
LeetCode #1
Problem: Two Sum


Approach 1: Brute Force
Time Complexity: O(n²)
Space Complexity: O(1) 

"""

class SolutionBruteForce(object):
    def twoSum(self, nums, target):

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

brute = SolutionBruteForce()

print(brute.twoSum([2, 7, 11, 15], 9))


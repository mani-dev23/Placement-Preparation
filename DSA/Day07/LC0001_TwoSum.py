"""
LeetCode #1
Problem: Two Sum

Approach 2: Hash Map
Time Complexity: O(n)
Space Complexity: O(n)

"""


class SolutionHashMap(object):
    def twoSum(self, nums, target):
        hashmap = {}

        for i, num in enumerate(nums):
            need = target - num

            if need in hashmap:
                return [hashmap[need], i]

            hashmap[num] = i

optimal = SolutionHashMap()

print(optimal.twoSum([2, 7, 11, 15], 9))
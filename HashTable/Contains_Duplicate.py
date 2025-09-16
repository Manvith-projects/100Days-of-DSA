# 217. Contains Duplicate

# Given an integer array nums, return true if any value appears at 
# least twice in the array, and return false if every element is distinct.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: true

from collections import Counter

class Solution:
    def Duplicate(self,nums):
        t=Counter(nums)

        for count in t.values():
            if count >1:
                return True

        return False

sol =Solution()
print(sol.Duplicate([1,2,3,1]))
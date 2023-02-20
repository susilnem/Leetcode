#Question

""""
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = {}
        for i, value in enumerate(nums):
            if target - value in output:
                return [output[target - value], i]
            else:
                output[value] = i


#Or 


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            if target - nums[i] in nums and nums.index(target - nums[i]) != i:
                return [i, nums.index(target - nums[i])]

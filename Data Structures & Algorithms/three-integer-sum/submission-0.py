class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #target is 0
        #must be 3 diff indices but can use the same value

        for index in range(len(nums)):
            target = 0 - nums(index)
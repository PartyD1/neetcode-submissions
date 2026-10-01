class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        found = {}
        for i in range(len(nums)):
            needed = target - nums[i]
            if needed in found:
                return [found[needed], i]
            found[nums[i]] = i        


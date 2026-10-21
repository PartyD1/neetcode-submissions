class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out_list = []
        nums.sort()

        for target in range(len(nums) - 2):
            if nums[target] > 0:
                break
            if target > 0 and nums[target] == nums[target - 1]:
                continue                          # 1. skip duplicate anchor

            left = target + 1
            right = len(nums) - 1

            while left < right:
                s = nums[left] + nums[right]

                if s == -nums[target]:
                    out_list.append([nums[target], nums[left], nums[right]])
                    right -= 1
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1                 # 2. skip duplicate left values
                elif s > -nums[target]:
                    right -= 1
                else:
                    left += 1

        return out_list
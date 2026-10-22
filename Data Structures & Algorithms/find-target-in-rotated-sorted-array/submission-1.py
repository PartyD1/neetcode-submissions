class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # [3,4,5,1,2] target = 1
        # mid = 5 left = 3 right = 2

        left = 0
        right = len(nums) - 1
        

        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            if nums[left] == target:
                return left
            if nums[right] == target:
                return right
            
            if target < nums[right]:
                left = mid + 1
            else:
                right = mid - 1

        return -1

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
           # if nums[left] == target:
           #     return left
           # if nums[right] == target:
           #     return right
            
            if nums[left] <= nums[mid]:
                #left side is sorted
                if nums[left] <= target < nums[mid]:
                    #target on the left side of mid
                    right = mid -1
                else:
                    left = mid + 1
                    #target on the right side of mid + unsorted
            else:
                #right side is sorted
                if nums[mid] < target <= nums[right]:
                    #target is between middle and right
                    left = mid + 1
                else: 
                    #target is left side + unsorted
                    right = mid - 1
                

        return -1

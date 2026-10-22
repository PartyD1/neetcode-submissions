class Solution:
    def findMin(self, nums: List[int]) -> int: 
        left = 0
        right = len(nums) -1
        mid = right // 2
        min = nums[left]

        #create the while condition that keeps going until 
        #until left and right are on the same value
        while left < right:
            mid = (right + left) // 2
            if nums[mid] > nums[right]:
                #minimum is on right of mid
                left = mid+1

            else:
                #minimum is either middle or left of middle
                right = mid

        return nums[left]


        



        
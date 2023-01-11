class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # what if nums.length == 1

        # find rotated index, k
        k, left, right = -1, 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[0] <= nums[mid]:
                left = mid + 1
            else:
                right = mid
            
        k = left

        # binary search on segment
        left = 0 if nums[0] <= target else k
        right = k if nums[0] <= target else len(nums) 
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        return -1
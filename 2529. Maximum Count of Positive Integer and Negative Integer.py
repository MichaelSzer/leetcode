class Solution:
    def maximumCount(self, nums: List[int]) -> int:

        # binary search
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < 0:
                left = mid + 1
            else:
                right = mid

        i, zeroes = left, 0
        while i < len(nums) and nums[i] == 0:
            zeroes += 1
            i += 1

        return max(left, len(nums) - left - zeroes)
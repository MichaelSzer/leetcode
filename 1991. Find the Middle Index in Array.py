class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        nums = [0] + nums
        leftside, rightside = 0, sum(nums)
        for i in range(1, len(nums)):
            leftside += nums[i - 1]
            rightside -= nums[i]

            if leftside == rightside:
                return i - 1

        return -1
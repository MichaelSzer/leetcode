class Solution:
    def averageValue(self, nums: List[int]) -> int:
        nums = tuple(filter(lambda x: x % 2 == 0 and x % 3 == 0, nums))
        return sum(nums) // len(nums) if len(nums) > 0 else 0
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 2, -1, -1):
            num = nums[i]
            
            # find next greater num
            next_greater = (-1, 101) #(index, value)
            for j in range(i + 1, len(nums)):
                if num < nums[j] and nums[j] < next_greater[1]:
                    next_greater = (j, nums[j])
            
            # found next greater
            if next_greater[0] != -1:
                # swap
                nums[next_greater[0]] = nums[i]
                nums[i] = next_greater[1]

                # sort
                nums[i + 1:] = sorted(nums[i + 1:])

                return

            # missing next greater, keep searching
            

        # next permutation not possible, restart order
        nums.sort()
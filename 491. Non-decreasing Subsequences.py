class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        sequence, ans = [], set()

        def createSolution(i = 0, smallest = None):
            nonlocal ans, nums, sequence
            if i == len(nums):
                if len(sequence) > 1: 
                    ans.add(', '.join(sequence))

                return

            # use given number
            if(smallest == None or nums[i] >= smallest):
                sequence.append(str(nums[i]))
                createSolution(i + 1, nums[i])
                sequence.pop()

            # skip number and avoid repeated sequences
            while(i < len(nums) - 1 and nums[i + 1] == nums[i]):
                i += 1
            
            createSolution(i + 1, smallest)

        createSolution()
        return list( map( lambda seq: map(lambda s_num: int(s_num), seq.split(', ') ), ans) )
class Solution:
    def numTrees(self, n: int) -> int:
        subtrees = [1]
        
        for i in range(1, n + 1):
            subtree = 0
            for j in range(0, i):
                subtree += subtrees[j] * subtrees[i - j - 1]

            subtrees.append(subtree)

        return subtrees[n]
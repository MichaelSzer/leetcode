from collections import defaultdict

class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        UAM_dict = defaultdict(lambda: set())
        for log in logs:
            UAM_dict[log[0]].add(log[1] - 1)
        
        UAM = [0] * k
        for mins in UAM_dict.values():
            UAM[len(mins) - 1] += 1

        return UAM
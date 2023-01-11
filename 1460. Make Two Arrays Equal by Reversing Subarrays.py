from collections import defaultdict

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        dict_target, dict_arr = defaultdict(int), defaultdict(int)
        for num in target:
            dict_target[num] += 1
        for num in arr:
            dict_arr[num] += 1
        
        if len(dict_target) != len(dict_arr):
            return False

        for key_t in dict_target:
            if dict_target[key_t] != dict_arr[key_t]:
                return False

        return True
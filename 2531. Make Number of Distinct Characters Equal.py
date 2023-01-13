from collections import defaultdict
from copy import copy

class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:

        word1_freq, word2_freq = defaultdict(int), defaultdict(int)
        for c in word1:
            word1_freq[c] += 1

        for c in word2:
            word2_freq[c] += 1

        for c1 in word1_freq:
            for c2 in word2_freq:
                # avoid changing dict size error
                word1_freq_c = copy(word1_freq)
                word2_freq_c = copy(word2_freq)

                # modify
                word1_freq_c[c1] -= 1
                word2_freq_c[c1] += 1
                word2_freq_c[c2] -= 1
                word1_freq_c[c2] += 1

                # check
                if len(tuple(filter(lambda c: word1_freq_c[c] > 0, word1_freq_c))) == len(tuple(filter(lambda c: word2_freq_c[c] > 0, word2_freq_c))):
                    return True

        return False
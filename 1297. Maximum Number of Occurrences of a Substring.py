from collections import defaultdict

class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        subs_ocurrence = defaultdict(int)

        # find substrings
        i = 0
        while i + minSize - 1 < len(s):
            j = i + minSize - 1
            letters = set({c for c in s[i:j + 1]})

            while j < len(s) and len(letters) <= maxLetters:
                letters.add(s[j])
                subs_ocurrence[s[i:j + 1]] += 1
                j += 1

            i += 1
                
        return max(subs_ocurrence.values()) if len(subs_ocurrence) else 0
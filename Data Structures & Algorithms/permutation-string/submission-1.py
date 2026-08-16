from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        char_count = Counter(s1)
        l = 0
        s1_len = len(s1)

        for r in range(len(s2)):
            new_char = s2[l:r+s1_len]

            new_char_count = Counter(new_char)

            if new_char_count == char_count:
                return True

            l+=1

        return False
        
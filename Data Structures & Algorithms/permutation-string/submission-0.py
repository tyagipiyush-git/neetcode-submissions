class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sorted_s1 = sorted(s1)
        l =0

        for r in range(len(s2)):
            print(s2[l:r+len(s1)])
            print(l, r+len(s1))
            new_char = sorted(s2[l:r+len(s1)])

            if new_char == sorted_s1:
                return True

            l+=1

        return False

        
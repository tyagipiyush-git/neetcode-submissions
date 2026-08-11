class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # Frequency array for 26 lowercase English letters
        counts = [0] * 26

        for char_s, char_t in zip(s, t):
            counts[ord(char_s) - 97] += 1  # 97 is ord('a')
            counts[ord(char_t) - 97] -= 1

        # Check if all 26 character balances are zero
        return all(x == 0 for x in counts)
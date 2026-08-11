class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counts = {}

        # Increment for characters in s, decrement for characters in t
        for char_s, char_t in zip(s, t):
            counts[char_s] = counts.get(char_s, 0) + 1
            counts[char_t] = counts.get(char_t, 0) - 1

        # Anagrams will have all frequency balances equal to 0
        return all(value == 0 for value in counts.values())
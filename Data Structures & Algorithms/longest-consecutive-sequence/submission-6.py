class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sets = set(nums)
        longest = 0

        for num in nums:
            if num-1 not in sets:
                current_num = num
                current_streak = 1

                while current_num+1 in sets:
                    current_streak +=1
                    current_num +=1

                if current_streak > longest:
                    longest = current_streak

        return longest

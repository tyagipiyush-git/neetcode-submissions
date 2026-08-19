class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)

        while l < r:
            m = l + ((r-l)//2)

            if nums[m] == target:
                return m
            elif nums[l] < target:
                l +=1
            else:
                r -=1

        return l if (l < len(nums) and nums[l] == target) else -1
        
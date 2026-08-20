class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r

        while l <= r:
            totaltime =0
            m = (l+r)//2

            for pile in piles:
                totaltime += math.ceil(pile/m)

            if totaltime <= h:
                res = m
                r = m-1

            else:
                l = m+1

        return res
        
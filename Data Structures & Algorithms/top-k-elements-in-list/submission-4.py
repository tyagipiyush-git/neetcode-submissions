from collections import Counter
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        if len(set(nums)) == k:
            return list(set(nums))

        counts = Counter(nums)
        sorted_count = sorted(counts, key=counts.get, reverse = True)

        values = sorted_count[:k]

        return values

        

        
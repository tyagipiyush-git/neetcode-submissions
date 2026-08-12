class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sort_nums = sorted(nums)
        res = []
        n = len(sort_nums)

        for i in range(len(sort_nums)):
            if i >0 and sort_nums[i] == sort_nums[i-1]:
                continue
            j = i+1
            k = n-1
            while j < k:
                sums = sort_nums[i] + sort_nums[j] + sort_nums[k]

                if sums == 0:
                    res.append([sort_nums[i],sort_nums[j],sort_nums[k]])

                    j +=1
                    k -=1

                    while j < k and sort_nums[j] == sort_nums[j-1]:
                        j +=1

                    while j <k and sort_nums[k] == sort_nums[k+1]:
                        k -=1

                elif sums < 0:
                    j +=1
                else:
                    k -=1

        return res
        
                           


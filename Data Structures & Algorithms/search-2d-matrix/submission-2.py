class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for ls in matrix:
            l =0
            r = len(ls)
            if ls[l] <= target <= ls[r-1]:
                while l < r:
                    print(l, r)
                    m = l + ((r-l)//2)
                    print('this is m', m)

                    if ls[m] == target:
                        return True
                    elif ls[m] < target:
                        l +=1
                    else:
                        r -=1
        return False
        
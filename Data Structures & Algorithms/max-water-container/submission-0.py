class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_volume =0

        left = 0
        right = len(heights)-1

        while left < right:
            minimum_height = min(heights[left], heights[right])
            volume = minimum_height*(right - left)

            if volume > max_volume:
                max_volume = volume
            
            if minimum_height == heights[left]:
                left+=1
            else:
                right -=1
        return max_volume
        
from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # kita main pake ide two pointers
        max_area = 0
        left, right = 0, len(heights)-1

        while left<right:
            width = right-left
            current_heights = min(heights[left],heights[right])
            # itung area skarang
            current_area = width*current_heights
            # itung maxnya
            max_area = max(max_area,current_area)

            # baru kita geser geserkan dia
            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
        return max_area
        
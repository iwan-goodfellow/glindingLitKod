from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # pertama kita harus pahami bahwa, utk nyari max areanya itu
        # cari si panjangnya itu kan indexnya yaa dari si j ke i (misal)
        # terus si tinggi itu adalah batas minimum tiap2 batang gtu yg ada di ujung ke ujung
        max_area = 0
        n = len(heights)

        for i in range(n):
            for j in range(i+1,n):
                width = j-i
                current_heigts = min(heights[i],heights[j])

                current_area = width * current_heigts
                max_area = max(max_area,current_area)
        return max_area
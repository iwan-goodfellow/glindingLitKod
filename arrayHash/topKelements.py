from collections import Counter

class Solution:
    def top_k_elements(nums):
        count = Counter(nums)
        # sorting deh
        sorted_key = sorted(count.keys(),key=lambda x: count[x], reverse=True)
        # ambil ssuai key yg diinput
        return sorted_key[:k]

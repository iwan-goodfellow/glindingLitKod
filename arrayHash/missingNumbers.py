class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        set_number = set(nums)

        for i in range(n+1):
            if i not in set_number:
                return i
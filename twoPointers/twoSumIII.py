from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()
        n = len(nums)

        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if nums[i]+nums[j]+nums[k] == 0:
                        res = [nums[i],nums[j],nums[k]]
                        result.add(tuple(res))

        return [list(i) for i in result]

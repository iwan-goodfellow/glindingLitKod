class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # gatau ideku lagi2 cuma loop wkwk
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]
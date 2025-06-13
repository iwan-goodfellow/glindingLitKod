# Example -> Input: nums = [1, 2, 3, 3]

# Output: true

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # kalo ini idenya adalah coba cekin satu satu dengan list yg diiter
        for num1 in range(len(nums)):
            for num2 in range(num1+1, len(nums)):
                if nums[num1] == nums[num2]:
                    return True
        
        return False
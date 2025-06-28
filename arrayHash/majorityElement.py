class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        count_elements = Counter(nums)

        for key,val in count_elements.items():
            if val > n/2:
                return key
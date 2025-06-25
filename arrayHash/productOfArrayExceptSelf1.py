class Solution:
    def productExceptSelf(self,nums: List[int]) -> List[int]:
        result = []

        # terus kita iter aja si i dlu
        for i in range(len(nums)):
            # initialize startingnya dengan 1
            product = 1
            # baru ambil si j
            for j in range(len(nums)):
                # ambil ketika dia itu indexnya gasama yaa
                if i!=j:
                    product*=nums[j]
            result.append(product)
        return result

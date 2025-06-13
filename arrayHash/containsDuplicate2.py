# ga terlalu optimal katanya, lesgo kita coba cara lain wkwk

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # cara lain kita coba pake set deh dia kan unik yaak
        seen = set()

        # kita ambilah si bocil2 num itu
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
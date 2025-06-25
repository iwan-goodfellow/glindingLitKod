class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0
        set_number = set(nums)

        for number in set_number:
            # cari brati dia gapnya harus selisih 1
            if number-1 not in set_number:
                current_number = number
                current_streak = 1

                while current_number+1 in set_number:
                    current_number+=1
                    current_streak+=1

                # bandingin berarti sekarang mana yg paling panjang yg current atau yg awal td uda ada
                longest_streak = max(longest_streak,current_streak)
        return longest_streak
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # initialize dlu kita punya kiri sama kanan
        left, right = 0, len(numbers)-1

        while left < right:
            # cari sama ga dgn targetnya penjumlahan kita
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                return [left+1,right+1]
            # kalo msi kurang brati geser kedepan aja si leftnya
            elif current_sum < target:
                left+=1
            else:
                right-=1

    
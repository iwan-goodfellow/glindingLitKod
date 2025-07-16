class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # jadi kan kita ambil dia itu dari 0 sampe n-3 kann kek gini nih _ | _ _ _ _ _ | _ _ _
        # itu nanti ada 3 pointers jadi si i, terus dibantu 2 pointers ujung ujung l dan r
        # di sort dlu
        nums.sort()
        result = []

        for i in range(len(nums)-2):
            # cek-in dlu kalo misal dia itu duplikat yaa kita skip
            if i>0 and nums[i]==nums[i-1]:
                continue
            # baru bikin pointer utk l dan r nya
            l,r = i+1,len(nums)-1

            while l<r:
                total = nums[i]+nums[l]+nums[r]
                # apakah dia hasilnya 0
                if total == 0:
                    result.append([nums[i],nums[l],nums[r]])
                    # baru jalan & cekin dia duplikat jg atau ga
                    while l<r and nums[l]==nums[l+1]:
                        l+=1
                    while r>l and nums[r]==nums[r-1]:
                        r-=1
                    # udah slesai skip-annya kita jalan lg
                    l+=1
                    r-=1
                elif total<0:
                    l+=1
                else:
                    r-=1
        return result

# langkah termudah wkwk yg ga kpikiran

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # cara lebih simple sebenernya adalah yaudah dicekin aja itu sortednya
        return sorted(s) == sorted(t)
    

# bisa lagi siih cara lain pake Counter gitu

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
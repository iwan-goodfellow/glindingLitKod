class Solution:
    def isPalindrome(self, s:str) -> bool:
        # pisahin dlu stringnya biar dia bersih
        s = ''.join(char.lower() for char in s if char.isalnum())

        # jalanin dia punya 2 pointer itu
        left, right = 0, len(s)-1
        while left<right:
            if s[left] != s[right]:
                return False
            left+=1
            right-=1
        return True
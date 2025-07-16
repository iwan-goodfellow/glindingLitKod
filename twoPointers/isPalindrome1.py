class Solution:
    def isPalindrome(self, s:str) -> bool:
        # palindrome klo dibalik huruf dan urutannya sama, kita bikin string baru aja yg udah clean
        s_clean = ''
        for char in s:
            if char.isalnum():
                s_clean+=char.lower()
        return s_clean == s_clean[::-1]
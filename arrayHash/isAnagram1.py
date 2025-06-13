class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # oke anagram itu kalo dia punya isi karakter yg sama (jelas jg brati dia lengthnya sama)
        s = sorted(s)
        t = sorted(t)

        if len(s) != len(t):
            return False 

        # cekin deh dia sama ato ga, ambil si list s sama list t masing-masing
        for i in range(len(s)):
            if s[i] != t[i]:
                return False
        return True
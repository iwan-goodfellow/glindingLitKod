class Solution:
    def group_anagrams(strs):
        # solve dengan dictionary basic (gtw hrusnya solved wkwk)
        grouped = {}
        # terus cek dlu ada ga key nya
        for word in strs:
            key = ''.join(sorted(word))
            if key not in word:
                grouped[key] = []

            grouped[key].append(word)
        
        return list(grouped.values())

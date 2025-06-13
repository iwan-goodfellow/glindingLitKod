# ===A bit explanation about collections library====
# -> ada counter, nah ini buat ngitung item didalam suatu yg iterable, misal di ana nah itu nanti dia Counter('ana') = {'a':2, 'n':1}
# -> terus ada lg defaultdict, ini sbnernya sama kek dict biasa cm otomatis kasi value wlupun key belum ada
from collections import defaultdict

class Solution:
    def grouped_anagram(arr):
        # jadi kita buat dlu dictnya
        grouped = defaultdict(list)

        # assign si key
        for word in arr:
            key = ''.join(sorted(word))
            # baru deh masukin si wordnya ke keys
            grouped[key].append(word)

        return list(grouped.values())

# STDIN                       Function
# -----                       --------
# 9                           n = 9
# 10 20 20 10 10 30 50 10 20  ar = [10, 10, 10, 10, 20, 20, | 20, 30, 50] -> out: 3
#                                                           ^ batas dia udah ga pasangan

# jadi soalnya tu nyuru kita nyari yg pasangan2 tu ada berapa, kek 10 itu ada 2, terus 20 ada 1 -> jadilah outnya 3
from collections import Counter

def sockMerchant(n, ar):
    total_pasangan = 0
    count_sock = Counter(ar)

    for values in count_sock.values():
        pasangan = values // 2
        total_pasangan+=pasangan
    print(total_pasangan) 

sockMerchant(9,[10, 20, 20, 10, 10, 30, 50, 10, 20])

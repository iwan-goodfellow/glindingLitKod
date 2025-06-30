# Oke kalo ini ada burung yg sedang migrate, terus kita disuru nyari burung paling banyak yg migrate jumlahnya
# terus smisal ada burung dengan jumlah yg sama, nanti ambil burung dengan tipe terkecil, smisal ada burung "tipe 2" -> 3 populasi, terus kebetulan si burung "tipe 4" -> 3 populasi
# nah kalo gitu casenya brati ambil si burung "tipe 2"

from collections import Counter

def migratoryBirds(arr):
    # karena kita mo ngitung banyaknya burung berati kita pake konsep Counter aja
    tipe_burung = jumlah_burung =  0
    counter_burung = Counter(arr)

    for tipe,jumlah in sorted(counter_burung.items()):
        if jumlah > jumlah_burung:
            jumlah_burung = jumlah
            tipe_burung = tipe
    
    print(tipe_burung)

migratoryBirds([1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]) # brati kan ini ada 2 tipe yg banyak dan sama wicis 3&4 tapi kita ambil tipe yg terkecil yaa jadi outnya nanti 3


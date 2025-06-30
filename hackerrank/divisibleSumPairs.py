# STDIN           Function
# -----           --------
# 6 3             n = 6, k = 3
# 1 3 2 6 1 2     ar = [1, 3, 2, 6, 1, 2] terus nanti outnya adalah -> 5
# dia itu nyari dimana si pasangan-pasangan ar kalo ditambahin itu habis dibagi sama si k,,,,

def divisibleSumPairs(n,k,ar):
    jumlah = 0
    for i in range(n):
        for j in range(i+1,n):
            if (ar[i]+ar[j])%k == 0:
                jumlah+=1
    print(jumlah)


divisibleSumPairs(6,3,[1, 3, 2, 6, 1, 2])
divisibleSumPairs(4,2,[1, 3, 2, 6, 1, 2])

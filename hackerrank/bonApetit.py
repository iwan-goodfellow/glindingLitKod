# jadi disini itu ada 2 bocil bobi ama ana, dia split bill. Misal bill = [2,4,6]
# tapi si ana gamau yg mahal (haha becanda🤣) jd dia gamakan bill[2] -> harusnya kalo ber2 awalnya bayar (2+4+6)/2=6 nah ini si anna kan cuma ambil 2 jadi bayar 6/2=3
# nah kan si bobi harus ngasi duit ke ana 3 ya,  itula outnya
# nanti tu ada masukan bill-> arr billnya, k-> index si ana gamau, b-> uang yg ana kasi ke bobi

def bonApetit(bill,k,b):
    gamau = bill[k]
    total_bill = sum(bill)
    ana_bill = (total_bill - gamau)//2
    sisa = b-ana_bill
    if sisa == 0:
        print('Bon Apetit')
    else:
        print(sisa)

bonApetit([3, 10, 2, 9],1,12)
bonApetit([3, 10, 2, 9],1,7)
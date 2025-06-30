# jadi disini itu si 2 kucing mo nangkep mouse nah mana yg lebih dekat sama si tikus itu yg diambil, sedangkan klo jarak kedua kucing itu sama yg kita return adalah si mousenya

def catAndMouse(kucing_x,kucing_y,tikus_z):
    if abs(tikus_z-kucing_x) < abs(tikus_z-kucing_y):
        # return 'Cat A'
        print('Cat A')
    elif abs(tikus_z-kucing_x) > abs(tikus_z-kucing_y):
        print('Cat B')
    else:
        print('Mouse C')
# kalo di hackerranknya ubah printnya ke return ya..
catAndMouse(10,11,12)
catAndMouse(10,12,11)

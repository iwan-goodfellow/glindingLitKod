# btw ini ku capital karena seru aja sii casenya wkwk
# UDDDUDUU -> outnya dia naik ke lembahnya sekali, kek gini ni gambarannya dengan ASCII
# lembah itu saat dimana dia dibawah 0 -> brati -1 nah kalo dia udah naik dari -1 brati udah naik dari lembah
# _/\      _
#    \    /
#     \/\/ 

def countingValleys(steps,path): #steps itu jumlahnya, path itu si list duud...  
    ketinggian = lembah = 0

    for step in range(steps):
        if path[step] == 'D':
            ketinggian-=1
        else: #berati yg uphill, ada 2 kmungkinan kan either dia naik lembah (keluar dari -1) atau yaudah naik aja
            if ketinggian == -1:
                lembah+=1
            ketinggian+=1
    print(f'Naik lembah {lembah}x')

countingValleys(8,['U','D','D','D','U','D','U','U'])
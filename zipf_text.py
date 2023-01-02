from collections import Counter
import matplotlib.pyplot as plt

from colors import colors

words = []
symbols = []

ss = Counter()
sc = Counter()

file_path = input()

with open(file_path,"r") as f1:
    s = f1.read()

    words = s.split()
    ss = Counter(words)

    for c in s:
        symbols.append(c)    
    sc = Counter(symbols)

    nsc = sorted(sc.items(), key=lambda x: x[1], reverse=1)
    nss = sorted(ss.items(), key=lambda x: x[1], reverse=1)

    c=0
    for i in nss:
        c=(c+1)%2
        col_fg = ''
        col_bg = ''
        if(c%2==0):
            col_fg = colors.fg.green
            col_bg = colors.bg.black
        elif(c%2==1):
            col_fg = colors.fg.cyan
            col_bg = colors.bg.gray
        print(col_fg, col_bg, colors.bold, f' {i[1]:10d}:', colors.reset, col_bg, f' {i[0]:30s} ', colors.reset, end="\n")

    print("\n\n\n")

    c=0
    for i in nsc:
        c=(c+1)%2
        col_fg = ''
        col_bg = ''
        if(c%2==0):
            col_fg = colors.fg.green
            col_bg = colors.bg.black
        elif(c%2==1):
            col_fg = colors.fg.cyan
            col_bg = colors.bg.gray
        print(col_fg, col_bg, colors.bold, f' {i[1]:10d}:' , colors.reset, col_bg,f'{i[0]:30s}', colors.reset, end="\n")


#graph functions


plt.plot( list(range(len(sc.items()))), sorted(list(sc.values()), reverse=1))


plt.show()


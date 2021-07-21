import os
accents='àáâãäåèéêëìíîïòóôõöøùúûüýÿ'
vocal='aaaaaaeeeeiiiioooooouuuuyy'
alphab='abcdefghijklmnopqrstuvwxyz '
num='0123456789'
string=input('Input: ')
string=string.lower()
strlist=[]
encr=''

#translation from accents to vocals
trad=string.maketrans(accents,vocal)
string=string.translate(trad)


for e in string:
    strlist.append(e)

n=0
cont=0
def calc(cont, n):
    if (cont%2) == 0:
        n=-n+1 # +1, +3, +5
        return n
    else:

        n=-n-1 # -2, -4, -6

        return n

for e in strlist:
    cont+=1
    n=calc(cont, n)
    if e in num:
        pos=num.find(e)
        add=pos+n
        if add>=10:
            while add>=10:
                add-=10
        if add<=-10:
            while add<=-10:
                add+=10

        encr+=num[add]


    else:
        if e in alphab:
            pos=alphab.find(e)
            add=pos+n
            if add>=27:
                while add>=27:
                    add-=27
            if add<=-27:
                while add<=-27:
                    add+=27
            encr+=alphab[add]
        else:
            encr+=e


print('Output:',encr)
os.system('pause')

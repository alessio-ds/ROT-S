import os, time

accents='àáâãäåèéêëìíîïòóôõöøùúûüýÿ'
vocal='aaaaaaeeeeiiiioooooouuuuyy'
alphab='abcdefghijklmnopqrstuvwxyz '
num='0123456789'

def encrypt(filename):
    start=time.time()
    with open(filename, mode='r', encoding='UTF-8') as f:
        string=f.read()


    string=string.lower()
    strlist=[]
    encr=''

    #translation from accents to vocals
    trad=string.maketrans(accents,vocal)
    string=string.translate(trad)


    for e in string:
        strlist.append(e)
    print('Encrypting ',str(len(strlist)),' bytes')
    n=0
    cont=0
    def calc(cont, n):
        if (cont%2) == 0:
            n=-n-1 # -2, -4, -6

            return n
        else:
            n=-n+1 # +1, +3, +5
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

    with open('encrypted.txt', mode='w', encoding='UTF-8') as c:
        c.write(encr)
    end=time.time()
    daprintare=str(len(strlist))+' bytes - '+(str(round(end-start, 6)))+'s'
    return(daprintare)
    os.system('pause')

def decrypt(filename):
    start=time.time()

    with open(filename, mode='r', encoding='UTF-8') as f:
        string=f.read()
    string=string.lower()
    strlist=[]
    encr=''

    #translation from accents to vocals
    trad=string.maketrans(accents,vocal)
    string=string.translate(trad)


    for e in string:
        strlist.append(e)
    print('Decrypting ',str(len(strlist)),' bytes')
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
    with open('decrypted.txt', mode='w', encoding='UTF-8') as c:
        c.write(encr)

    end=time.time()
    daprintare=str(len(strlist))+' bytes - '+(str(round(end-start, 6)))+'s'
    return(daprintare)
    os.system('pause')

#le funzioni ritornano round(end-start, 6)


a1=encrypt('100bytes.txt')
a2=encrypt('250bytes.txt')
a3=encrypt('500bytes.txt')
a4=encrypt('1000bytes.txt')
a5=encrypt('2500bytes.txt')
a6=encrypt('5000bytes.txt')
a7=encrypt('10k_bytes.txt')
a8=encrypt('25k_bytes.txt')
a9=encrypt('50k_bytes.txt')
a10=encrypt('100k_bytes.txt')

print('\n')

b1=decrypt('100bytes.txt')
b2=decrypt('250bytes.txt')
b3=decrypt('500bytes.txt')
b4=decrypt('1000bytes.txt')
b5=decrypt('2500bytes.txt')
b6=decrypt('5000bytes.txt')
b7=decrypt('10k_bytes.txt')
b8=decrypt('25k_bytes.txt')
b9=decrypt('50k_bytes.txt')
b10=decrypt('100k_bytes.txt')

print('\nDone. Check "results.txt".\n')
with open('results.txt', mode='r') as f:
    print(f.read())

testo='ENCRYPT:\n'+a1+'\n'+a2+'\n'+a3+'\n'+a4+'\n'+a5+'\n'+a6+'\n'+a7+'\n'+a8+'\n'+a9+'\n'+a10+'\n\n'+'DECRYPT:\n'+b1+'\n'+b2+'\n'+b3+'\n'+b4+'\n'+b5+'\n'+b6+'\n'+b7+'\n'+b8+'\n'+b9+'\n'+b10
with open('results.txt', mode='w') as f:
    f.write(testo)

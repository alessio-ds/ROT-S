import os, time
accents='àáâãäåèéêëìíîïòóôõöøùúûüýÿ'
vocal='aaaaaaeeeeiiiioooooouuuuyy'
alphab='abcdefghijklmnopqrstuvwxyz '
num='0123456789'

print('IF YOU WANT TO ENCRYPT, PUT A "decrypted.txt" FILE IN THE SAME FOLDER AS THIS PROGRAM')
print('IF YOU WANT TO DECRYPT, PUT A "encrypted.txt" FILE IN THE SAME FOLDER AS THIS PROGRAM')
dom=input('Do you want to encrypt or decrypt? E/D: ')
if dom=='E' or dom=='e':

    start=time.time()

    with open('decrypted.txt', mode='r', encoding='UTF-8') as f:
        string=f.read()


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
            n=-n-1 # -2, -4, -6

            return n
        else:
            n=-n+1 # +1, +3, +5
            return n

    for e in strlist:
        print('Loading:', abs(n)+1,'out of',len(strlist))
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
    print('\nDone')
    end=time.time()
    print('It took: ', round(end-start, 2), 's\n')
    os.system('pause')






else:
    if dom=='D' or dom=='d':

        start=time.time()

        with open('encrypted.txt', mode='r', encoding='UTF-8') as f:
            string=f.read()
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
            print('Loading:', abs(n)+1,'out of',len(strlist))
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

        print('\nDone')
        end=time.time()
        print('It took: ', round(end-start, 2), 's\n')
        os.system('pause')

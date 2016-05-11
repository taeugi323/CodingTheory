from Galois import add, multiple, scalar_mul, compare

def check_with_coset(g,his,delt):
    for a in range(0,2):
        for b in range(0,2):
            for c in range(0,2):
                temp = add(scalar_mul(a,g[0]),scalar_mul(b,g[1]))
                elem = add(temp,scalar_mul(c,g[2]))
                elem = add(elem,delt)
                if elem not in his:
                    his.append(elem)
                    print elem
                else:
                    return 0
    return 1

G = [
        [1,0,0,0,1,1],
        [0,1,1,0,0,1],
        [0,0,1,1,1,0]
    ]

H = [
        [0,1,1,1,0,0],
        [1,1,1,0,1,0],
        [1,1,0,0,0,1]
    ]

Ht = [
        [0,0,1],
        [0,1,0],
        [0,1,1],
        [1,0,0],
        [1,1,0],
        [1,1,1]
    ]

history = []
codeword = []

" part of 3.(a) "

print "---- codewords ----\n"
check_with_coset(G,codeword,[0,0,0,0,0,0])

print "\n---- zero bits check ----\n"
temp = [0,0,0,0,0,0]
check_with_coset(G,history,temp)
print "syndrome is",multiple(H,temp)
print "Known vectors :",len(history),"\n"

print "---- one bits check ----\n"
for i in range(0,6):
    temp[i] = 1
    print "Coset of",temp,"\n"
    if check_with_coset(G,history,temp):
        print "syndrome is",Ht[i]
        print "Known vectors :",len(history),"\n"
    temp = [0,0,0,0,0,0]

print "\n---- two bits check ----"
for i in range(0,5):
    for j in range(i+1,6):
        temp[i]=1
        temp[j]=1
        print "Coset of",temp
        if check_with_coset(G,history,temp):
            print "syndrome is",add(Ht[i],Ht[j])
            print "Known vectors :",len(history),"\n"
        else:
            print "This is already in an another coset\n"
        temp = [0,0,0,0,0,0]
        

" part of 3.(b) and 3.(c) "
print "\n----- Error Correcting -----"
for a1 in range(0,2):
    for a2 in range(0,2):
        for a3 in range(0,2):
            for a4 in range(0,2):
                for a5 in range(0,2):
                    for a6 in range(0,2):
                        temp = [a1,a2,a3,a4,a5,a6]
                        ans = compare(temp,codeword)
                        if len(ans) == 1:
                            print temp,"is decoded to",ans[0]
                        elif len(ans) == 0:
                            print temp,"Impossible to decode"
                        else:
                            print temp,"Double or more matched. num is",len(ans),"Cannot be decoded"



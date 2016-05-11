from Galois import add, multiple, scalar_mul

g1 = [1,0,0,0,0,1,1]
g2 = [0,1,0,0,1,0,1]
g3 = [0,0,1,0,1,1,0]
g4 = [0,0,0,1,1,1,1]

codeword = []

for a1 in range(2):
    for a2 in range(2):
        for a3 in range(2):
            for a4 in range(2):
                temp1 = add(scalar_mul(a1,g1),scalar_mul(a2,g2))
                temp2 = add(scalar_mul(a3,g3),scalar_mul(a4,g4))
                codeword.append(add(temp1,temp2))


# self-orthogonal check for Hamming code
ortho_true = []
ortho_false = []

for i in range(len(codeword)):
    for j in range(i+1,len(codeword)):
        real_temp = [codeword[i]]   # to use multiple module. Its param is (double list, list)
        temp = multiple(real_temp,codeword[j]) 
        if temp == [0]:
            ortho_true.append((codeword[i],codeword[j]))
        else:
            ortho_false.append((codeword[i],codeword[j]))

print "-----Orthogonal codes-----"
for i in ortho_true:
    print i
print "number :", len(ortho_true)

print "\n-----Non_orthogonal codes-----"
for i in ortho_false:
    print i
print "number :", len(ortho_false)

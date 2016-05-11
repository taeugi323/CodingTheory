from Galois import add, multiple, scalar_mul, compare

g1 = [1,0,0,0,0,1,1]
g2 = [0,1,0,0,1,0,1]
g3 = [0,0,1,0,1,1,0]
g4 = [0,0,0,1,1,1,1]

number=0
list_codeword = []

print "codeword list\n"
for a1 in range(2):
    for a2 in range(2):
        for a3 in range(2):
            for a4 in range(2):
                temp1 = add(scalar_mul(a1,g1),scalar_mul(a2,g2))
                temp2 = add(scalar_mul(a3,g3),scalar_mul(a4,g4))
                codeword = add(temp1,temp2)
                print str(number)+".",codeword
                number += 1
                list_codeword.append(codeword)

print "\nmatch information"
number = 0
for a1 in range(2):
    for a2 in range(2):
        for a3 in range(2):
            for a4 in range(2):
                for a5 in range(2):
                    for a6 in range(2):
                        for a7 in range(2):
                            temp = [a1,a2,a3,a4,a5,a6,a7]
                            ans = compare(temp,list_codeword)
                            if len(ans) == 1:
                                print temp,"("+str(number)+") matches",ans[0],"(index",list_codeword.index(ans[0]),")"
                            else:
                                print "Something wrong",temp,ans
                            number += 1

# Addition of two vectors over GF(2)
def add(A,B):
    res = []
    for i in range(len(A)):
        if A[i] == B[i]:
            res.append(0)
        else:
            res.append(1)

    return res

# Multiplication of two matrices
def multiple(A,B):  # B is one column matrix 
    res = []
    for elem in A:
        cnt=0
        for i in range(len(B)):
            if elem[i] & B[i]:
                cnt+=1
        if cnt%2 == 0:
            res.append(0)
        else:
            res.append(1)

    return res

# Scalar multiplication over GF(2)
def scalar_mul(t,A):
    res = []
    for i in A:
        res.append(t&i)

    return res

# Compare two vectors and return the number of different bits
def compare(A,ls):
    res = []
    for elem in ls:
        cnt = 0
        for i in range(len(elem)):
            if A[i] != elem[i]:
                cnt += 1

        if cnt <= 1:
            res.append(elem)

    return res

# Divide A by B and return the quotient and remainder
def divide(A,B):
    while B[0] == 0:
        B.remove(B[0])

    res = [0 for i in range(len(A)-len(B)+1)]

    idx_A = 0
    idx_res = 0
    for i in range(len(B), len(A)+1):
        if A[idx_A] == 1:
            A[idx_A:i] = add(A[idx_A:i],B)
            res[idx_res] = 1

        idx_res += 1
        idx_A += 1
        #print "A is",A,"\nres is",res
    return [res,A]

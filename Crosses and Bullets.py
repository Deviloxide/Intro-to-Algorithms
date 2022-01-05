import numpy as np

def rhythm(test_string):
    test_string = "xxxxxxx*****"

    crosses = test_string.count('x')
    bullets = test_string.count('*')
    a = crosses + bullets

    A = np.array(list(crosses * "x" + bullets * "*"), dtype=object)
    print(A)
    print(A.shape)


    if crosses > bullets:
        b = crosses
    else:
        b = bullets

    q = a // b
    r = a % b

    test_list = []

    test_list.append([a,q,b,r])

    print(A)

    while r != 0 and r != 1:
        a = b
        b = r
        q = a // b
        r = a % b
        test_list.append([a, q, b, r])

        for i in range(0, q):
            row = np.array(['*', '*', '*', '*', '*'])
            A = np.vstack([A, row])

    return test_list

print(rhythm("test_string"))

# xxxxxxx*****

# xxxxxxx
# *****

# xxx
# ***
# xx
# xx
# **

#A = [[A[0][:-r]], [A[0][-r:]]]
#print(A)

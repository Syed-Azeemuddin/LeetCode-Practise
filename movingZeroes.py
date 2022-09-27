a_list = [86,77,0,0,0,2,3,5,6,7,1]

#[8,3,12,0,0]



def movZero(a_list):
    n = 0
    j = len(a_list)

    for i in a_list:
        if i != 0:
            a_list[n] = i
            n += 1
        
    for x in range (n, j):
        a_list[x] = 0

    return a_list
print(movZero(a_list))
        




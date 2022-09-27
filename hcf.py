import gc


def gcf(n1, n2):

    gcf = 0

    if(n1 > n2):
        small = n2
    elif(n2 > n1):
        small = n1
    elif(n1 == 0 or n2 == 0):
        return gcf
    else:
        return -1
    
    for i in range(1, small + 1):
        if( n1 % i == 0 and n2 % i == 0):
            gcf = i
    
    return gcf

print(gcf(44,4))
def list_primes(n):

    ls = []

    s = [True]*(n+1)

    for i in range(2,n+1):
        if(s[i] and s[i]%2==1):
            ls.append(i)
            for j in range(i,n+1,i):
                s[j] = False
    
    return ls

print(list_primes(1000000))



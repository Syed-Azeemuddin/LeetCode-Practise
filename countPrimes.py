import math
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<2:
            return 0
        
        prime = [True]*n
        prime[0] = prime[1] = False
        
        for i in range(2,int(math.ceil(math.sqrt(n)))):
            if prime[i]:
                for j in range(i*i,n,i):
                    prime[j] = False
        return sum(prime)
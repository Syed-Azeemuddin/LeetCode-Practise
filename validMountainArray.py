from typing import List

from typing import List
arr = [1,3,2]


class Solution:
    def isValid(self, arr:List[int]):
        a = len(arr)
        i = 1

        if(a < 3):
            return False

        while (i < a and arr[i] >= arr[i-1]):
            i += 1

        if (i == 1 or i == a - 1):
            return False

        while (i < a and arr[i] <= arr[i - 1]):
            i += 1

        return i == a
    

        
        
                
        

s = Solution()

answ = s.isValid(arr)

print(answ)
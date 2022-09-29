#finding first and last position of an element in a sorted array



from typing import List


class Solution:

    def getLeftPosition(self,arr,n):
        l = 0
        r = len(arr)-1

        while(l<=r):
            mid = (l+r)//2
            if(arr[mid]==n):
                if(mid-1 >=0 and arr[mid-1]!=n or mid==0):  
                    return mid
                r = mid-1
            elif(arr[mid]>n):
                r = mid-1
            else:
                l = mid+1
        return -1

    def getRightPosition(self,arr,n):
        l = 0
        r = len(arr)-1

        while(l<=r):
            mid = (l+r)//2
            if(arr[mid]==n):
                if((mid+1 < len(arr) and arr[mid+1]!=n) or mid==len(arr)-1):
                    return mid
                l = mid+1
            elif(arr[mid]>n):
                r = mid-1
            else:
                l = mid+1
        return -1

    def positions(self,arr:List[int],n: int)->List[int]:

        left = self.getLeftPosition(arr, n)
        right = self.getRightPosition(arr, n)

        return [left,right]


s = Solution()

answ = s.positions([2,2,3,4,5,6,7,8,8,10],8)

print(answ)
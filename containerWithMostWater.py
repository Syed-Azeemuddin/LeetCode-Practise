from turtle import right
from typing import List

class Solution:

    def mxArea(self, height: List[int]) -> int:

        l = 0
        r = len(height) - 1
        maxArea = 0

        while(l < r):

            maxArea = max(maxArea, min(height[l],height[r])*(r-l))

            if(height[l] < height[r]):
                l += 1
            else:
                r -= 1
        return maxArea


s = Solution()

answ = s.mxArea([1,8,6,2,5,4,8,3,7])

print(answ)
from typing import List


class Solution(object):

    def majorityNumber(self, nums:List[int])->int:

        m = {}
        for num in nums:
            m[num] = m.get(num,0)+1
        
        for num in nums:
            if(m[num]> len(nums)/2):
                return num


s  = Solution()
answ = s.majorityNumber([2,2,1,1,1,2,2])

print(answ)
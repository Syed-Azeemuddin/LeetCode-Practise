from typing import List


class Solution:

    def sum4answer(self, nums1:List[int],nums2:List[int],nums3:List[int],nums4:List[int]):
        m = {}
        ans = 0

        l1 = len(nums1)
        l2 = len(nums2)
        l3 = len(nums3)
        l4 = len(nums4)

        for i in range(0,l1):
            x = nums1[i]
            for j in range(0,l2):
                y = nums2[j]
                if x+y not in m:
                    m[x+y] = 0
                m[x+y]+=1
        
        for i in range(0,l3):
            x = nums3[i]
            for j in range(0,l4):
                j = nums4[j]
                target = -(x+y)
                if target in m:
                    ans += m[target]
        
        return ans
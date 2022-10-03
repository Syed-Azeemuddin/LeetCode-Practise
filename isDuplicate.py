from typing import List


class Solution:

    def isDuplicate(self, nums: List[int]) -> bool:

        m = {}
        n = len(nums)

        for i in range(0, n):
            if nums[i] in m:
                return True
            m[nums[i]] = i

        return False

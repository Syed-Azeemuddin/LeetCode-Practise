class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        m = {}
        n = len(nums)

        for i in range(0,n):
            x = target - nums[i]
            if x in m:
                return [m[x],i]
            
            m[nums[i]] = i
        
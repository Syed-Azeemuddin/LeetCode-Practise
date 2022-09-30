#missing number

from typing import List


class Solution:

    def missingNumber(self,arr:List[int])->int:
        """Using Gauss Formula:
            sum of elements upto n = n*(n+1)/2

            complexity: O(N)
            space: O(1)
        Args:
            arr (List): array of numbers

        Returns:
            int: missing number
        """
        l = len(arr)
        real_sum = l*(l+1)/2
        current_sum = sum(arr)

        return int(real_sum - current_sum)


s = Solution()

answ = s.missingNumber([3,0,1])

print(answ)

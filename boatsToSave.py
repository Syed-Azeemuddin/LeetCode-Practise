from typing import List

class Solution:

    def numRescueBoats(self, people:List[int], limit: int) -> int :
        people.sort()

        left = 0
        right = len(people) - 1
        boats_num = 0

        while(left <= right):
            if(left == right):
                boats_num += 1
                break

            if(people[left] + people[right] <= limit):
                left += 1
            
            right -= 1
            boats_num += 1
        
        return boats_num


s = Solution()

answ = s.numRescueBoats([3,2,2,1],3)

print(answ)
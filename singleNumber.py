from typing import List


class Solution:
    def single(self,arr:List[int])->int:
        """Formula:
            2*(a+b+c)#summation of unique elements - (a+a+b+b+c)#summation of all elements = c
            2*(a+b+c)-(a+a+b+b+c)=c
            which is:
                    2*Unique_nums * all_sum = ans
            
            TimeComplexity: O(2*N) = O(N)  {we pass over the input array once; we do a separate pass over set once}


        Args:
            arr (List[int]): Given a non-empty array of integers nums, every element appears twice except for one. 
            Find that single one. 

        Returns:
            int: single one
        
        """

        return 2*sum(set(arr)) - sum(arr)



from typing import List

class Solution:
    def plsadfsadf(self, digits: List[int]) -> List[int]:

        ## Brute Force
        # result = []
        # multiplier = 1
        # sum = 0
        # for i in range(len(digits)-1, -1, -1):
        #     sum += digits[i]*multiplier
        #     multiplier*=10
        # sum+=1
        # for s in str(sum):
        #     result.append(int(s))
        # return result

        ## Optimal Solution
        carry = 0
        for i in range(len(digits)-1, -1, -1):
            print("Testing ",i," th digit ",digits[i])
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        result = [0]*(len(digits)+1)
        result[0] = 1
        return result

s = Solution()
print(s.plsadfsadf([1,2,3]))
print(s.plsadfsadf([9,9,9]))
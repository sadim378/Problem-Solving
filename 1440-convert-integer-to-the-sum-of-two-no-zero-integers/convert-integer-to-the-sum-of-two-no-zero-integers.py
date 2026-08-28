from typing import List

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        
        def noZero(num):
            return '0' not in str(num)

        for a in range(1, n):
            b = n - a

            if noZero(a) and noZero(b):
                return [a, b]
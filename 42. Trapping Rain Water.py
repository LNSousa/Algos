'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, 

compute how much water it can trap after raining.
'''

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0: return 0
        
        n, m  = 0, len(height)-1
        nMax, mMax = height[n], height[m]
        final = 0

        while n < m:
            if nMax <= mMax:
                n += 1
                nMax = max(nMax, height[n])
                final += nMax - height[n]
            else:
                m -= 1
                mMax = max(mMax, height[m])
                final += mMax - height[m]

        return final
    
print(Solution.trap(Solution, [0,1,0,2,1,0,1,3,2,1,2,1]))
print(Solution.trap(Solution, [4,2,0,3,2,5]))
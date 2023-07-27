'''
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
'''

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        max = 0
        while l < r:
            tempMax = min(height[l], height[r]) * (r - l)
            if tempMax > max:
                max = tempMax
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max
    

print(Solution.maxArea(Solution, [1,8,6,2,5,4,8,3,7]))
print(Solution.maxArea(Solution, [1,1]))
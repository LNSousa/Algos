'''
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. 
The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. 
Each hour, she chooses some pile of bananas and eats k bananas from that pile. 
If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.
'''
from typing import List
import math

def minEatingSpeed(piles: List[int], h: int) -> int:
    l, r = 1, max(piles)
    
    pointer = r

    while l <= r:
        hours = 0
        k = (l + r) // 2
        for i in piles:
            hours += math.ceil(i / k)

        if hours <= h:
            pointer = min(pointer, k)
            r = k - 1
        else:
            l = k+ 1


    return pointer







print(minEatingSpeed([3,6,7,11], 8))
print(minEatingSpeed([30,11,23,4,20], 5))
print(minEatingSpeed([30,11,23,4,20], 6))
print(minEatingSpeed([312884470], 312884469))
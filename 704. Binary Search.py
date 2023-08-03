'''
Given an array of integers nums which is sorted in ascending order, and an integer target, 
write a function to search target in nums. If target exists, then return its index. 
Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
'''

from typing import List
def search(nums: List[int], target: int) -> int:
        idx = int(len(nums) / 2)
        
        if nums[idx] < target:
                while nums[idx] != target:
                        idx += 1
                        if idx == len(nums):
                                return -1
                return idx
        else:
                while nums[idx] != target:
                        idx -= 1
                        if idx == -1:
                                return -1
                return idx
                
                        

print(search([-1,0,3,5,9,12], 9))
print(search([-1,0,3,5,9,12], 2))
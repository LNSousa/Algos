'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
'''

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results=[]

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue

            l, r = i+1, len(nums) - 1
            while l < r:
                result = a + nums[l] + nums[r]
                if result < 0:
                    l+=1
                elif nums[l] + nums[r] + nums[i] > 0:
                    r-=1
                else:
                    results.append([a, nums[l], nums[r]])
                    l+=1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

        return results


Solution.threeSum(Solution, nums=[-1,0,1,2,-1,-4])
Solution.threeSum(Solution, nums=[0,1,1])
Solution.threeSum(Solution, nums=[0,0,0])
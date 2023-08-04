'''
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
'''
from typing import List


def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    for i in range(len(matrix)):
        last = len(matrix[i])-1
        if matrix[i][0] <= target <= matrix[i][last]:
            for j in range(len(matrix[i])):
                if matrix[i][j] == target:
                    return True
    
    return False

matrix, target1, target2 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3, 13

print(searchMatrix(matrix, target1))
print(searchMatrix(matrix, target2))
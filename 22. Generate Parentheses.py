'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
'''
from typing import List
def generateParenthesis(n: int) -> List[str]:
        arr = []
        temp = []

        def recursion(l, r):
                if l == r == n:
                        arr.append("".join(temp))
                        return
                
                if l < n:
                        temp.append("(")
                        recursion(l+1, r)
                        temp.pop()

                if r < l:
                        temp.append(")")
                        recursion(l, r+1)
                        temp.pop()

        recursion(0, 0)
        return arr
        

print(generateParenthesis(3))
print(generateParenthesis(7))
print(generateParenthesis(1))
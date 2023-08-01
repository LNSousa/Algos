from typing import List
def evalRPN(tokens: List[str]) -> int:
        stack = []
        total = int(tokens[0])

        for i in range(len(tokens)):
            if tokens[i].lstrip('-').isdigit():
                stack.append(int(tokens[i]))
            else:
                second = stack.pop()
                first = stack.pop()

                if tokens[i] == "+":
                    total = first + second
                elif tokens[i] == "-":
                    total = first - second
                elif tokens[i] == "*":
                    total = first * second
                else:
                    total = int(first / second)
                print("total ", total)
                stack.append(total)
                
        return total

print(evalRPN(["2","1","+","3","*"]))
print(evalRPN(["4","13","5","/","+"]))
print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))

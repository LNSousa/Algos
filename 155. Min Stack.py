'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack(): initializes the stack object.
void push(int val): pushes the element val onto the stack.
void pop(): removes the element on the top of the stack.
int top(): gets the top element of the stack.
int getMin(): retrieves the minimum element in the stack.

You must implement a solution with O(1) time complexity for each function.
'''

class MinStack:

    def __init__(self):
        self.head = None

    def push(self, val: int) -> None:
        node = {"value": val, "next": None}

        if not self.head:
            self.head = node
            return self
        else:
            oldHead = self.head
            self.head = node
            self.head["next"] = oldHead
            return self

    def pop(self) -> None:
        if not self.head:
            return self
        else:
            self.head = self.head["next"]

    def top(self) -> int:
        return self.head["value"]

    def getMin(self) -> int:
        runner, min = self.head, self.head["value"]
        if not self.head:
            return self
        while runner:
            if runner["value"] < min:
                min = runner["value"]
            runner = runner["next"]

        return min
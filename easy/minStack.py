"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

    push(x) -- Push element x onto stack.
    pop() -- Removes the element on top of the stack.
    top() -- Get the top element.
    getMin() -- Retrieve the minimum element in the stack.

Example:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
"""

class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_stack = []

    def push(self, x: int) -> None:
        self.min_stack.append(x)

    def pop(self) -> None:
        if self.min_stack == []:
            return null
        else:
            return self.min_stack.pop()

    def top(self) -> int:
        if self.min_stack == []:
            return null
        else:
            return self.min_stack[-1]

    def getMin(self) -> int:
        if self.min_stack == []:
            return null
        else:
            return min(self.min_stack)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

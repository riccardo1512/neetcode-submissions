class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            match t:
                case '+':
                    stack.append(stack.pop() + stack.pop())
                case '-':
                    a, b = int(stack.pop()), int(stack.pop())
                    stack.append(b - a)
                case '*':
                    stack.append(stack.pop() * stack.pop())
                case '/':
                    a, b = int(stack.pop()), int(stack.pop())
                    stack.append(int(b / a))
                case _:
                    stack.append(int(t))
                
        return stack.pop()
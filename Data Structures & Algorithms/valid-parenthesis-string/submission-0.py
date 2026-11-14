class Solution:
    def checkValidString(self, s: str) -> bool:
        min_open = 0 # min number of paretheses opened that still need to be closed
        max_open = 0 # max number of paretheses opened that still need to be closed

        for c in s:
            if c == '(':
                min_open += 1
                max_open += 1
            elif c == ')':
                min_open -= 1
                max_open -= 1
            else:
                min_open -= 1
                max_open += 1

            if max_open < 0:
                return False

            min_open = max(min_open, 0)

        return min_open == 0
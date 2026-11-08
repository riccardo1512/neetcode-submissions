class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t, b = 0, len(matrix) - 1

        while t <= b:
            m = (t + b) // 2

            line = matrix[m]

            if line[0] <= target <= line[len(line) - 1]:

                l, r = 0, len(line) - 1

                while l <= r:
                    m = (l + r) // 2

                    if line[m] == target:
                        return True
                    elif target < line[m]:
                        r = m - 1
                    else:
                        l = m + 1
                
                return False
            
            if target < line[0]:
                b = m - 1
            else:
                t = m + 1
        
        return False
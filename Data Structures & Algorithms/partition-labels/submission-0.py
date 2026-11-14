class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_idx = {c : i for i, c in enumerate(s)}

        res = []
        end = 0
        size = 0

        for i, c in enumerate(s):
            size += 1

            end = max(end, last_idx[c])
            
            if i == end:
                res.append(size)
                size = 0
        
        return res
        
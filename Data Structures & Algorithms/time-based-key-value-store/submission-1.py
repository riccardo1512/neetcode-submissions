class TimeMap:

    def __init__(self):
        self.d = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ""
        
        arr = self.d[key]
        l, r = 0, len(arr) - 1
        res = ""

        while l <= r:
            m = (l + r) // 2

            t, v = arr[m]
            
            if t <= timestamp:
                res = v
                l = m + 1
            else:
                r = m - 1


        return res
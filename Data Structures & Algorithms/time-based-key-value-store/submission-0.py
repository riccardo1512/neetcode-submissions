class TimeMap:

    def __init__(self):
        self.keyMap = defaultdict(list)

        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keyMap[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        arr = self.keyMap[key]

        l, r = 0, len(arr) - 1
        res = ""

        while l <= r:
            m = (l + r) // 2

            t, v = arr[m]

            if t <= timestamp:
                res = v
                l = m + 1
            if timestamp < t:
                r = m - 1
        return res
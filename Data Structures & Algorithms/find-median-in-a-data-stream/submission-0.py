class MedianFinder:

    def __init__(self):
        self.data = []
        

    def addNum(self, num: int) -> None:
        self.data.append(num)
        

    def findMedian(self) -> float:
        self.data.sort()
        l = len(self.data)
        
        if l % 2 != 0:
            return self.data[l//2]
        else:
            return (self.data[l//2 - 1] + self.data[l//2] ) / 2

        
        
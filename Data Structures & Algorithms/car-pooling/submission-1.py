class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # trips[i] = [numPassengers[i], from[i], to[i]]
        trips.sort(key = lambda x : x[1])
        car = [] # destination : numPassengers
        
        position = 0
        for numPassengers, start, end in trips:
            position = start

            while car and car[0][0] <= position:
                d, num = heapq.heappop(car)
                capacity += num

            if numPassengers > capacity:
                return False
            else:
                capacity -= numPassengers
                heapq.heappush(car, (end, numPassengers))

        return True

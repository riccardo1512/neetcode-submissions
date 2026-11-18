class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events = []
        for numPassengers, start, dest in trips:
            events.append((start, numPassengers))
            events.append((dest, -numPassengers))

        events.sort()
        
        current_passengers = 0
        for place, numPassengers in events:
            current_passengers += numPassengers
            if current_passengers > capacity:
                return False

        return True
        
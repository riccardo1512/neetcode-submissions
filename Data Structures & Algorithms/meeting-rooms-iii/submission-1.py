class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        count = [0] * n


        free_rooms = list(range(n)) # index
        heapq.heapify(free_rooms)
        busy_rooms = []             # end_time, index

        for start, end in meetings:
            while busy_rooms and start >= busy_rooms[0][0]:
                end_time, index = heapq.heappop(busy_rooms)
                heapq.heappush(free_rooms, index)

            duration = end - start

            if free_rooms:
                index = heapq.heappop(free_rooms)
                heapq.heappush(busy_rooms, (end, index))
                count[index] += 1
            else:
                end_time, index = heapq.heappop(busy_rooms)
                heapq.heappush(busy_rooms, (end_time + duration, index))
                count[index] += 1

        return count.index(max(count))
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        ordered_task = [[tasks[x][0], tasks [x][1], x] for x in range(len(tasks))] # [enqueueTime, processingTime, original_idx]
        ordered_task.sort()

        ready = [] # (processingTime, original_idx)
        res = []    # original_idx

        time = 0
        i = 0       # index for ordered_task
        while len(res) < len(ordered_task):
            while i < len(ordered_task) and time >= ordered_task[i][0]:
                enqueueTime, processingTime, original_idx = ordered_task[i]
                heapq.heappush(ready, (processingTime, original_idx))
                i += 1

            if ready:
                processingTime, original_idx = heapq.heappop(ready)
                time += processingTime
                res.append(original_idx)
            else:
                time += 1

        return res

            
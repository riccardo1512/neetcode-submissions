class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x : x[0] - x[1])

        l = len(costs) // 2
        first = sum(x[0] for x in costs[:l])
        second = sum(x[1] for x in costs[l:])

        return first + second
        
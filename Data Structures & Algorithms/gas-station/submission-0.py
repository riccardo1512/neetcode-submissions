class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        start = 0
        cur_tank = 0

        for i in range(len(gas)):
            cur_tank += gas[i] - cost[i]

            if cur_tank < 0:
                start = i + 1
                cur_tank = 0
        
        return start
        
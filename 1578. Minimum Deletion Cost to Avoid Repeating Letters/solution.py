class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        stackl = [""]
        stackp = [0]
        costf = 0
        for index, leter in enumerate(s):
            if leter == stackl[-1]:
                if cost[index] > stackp[-1]:
                    costf += stackp.pop(-1)
                    stackp.append(cost[index])
                    stackl.pop(-1)
                    stackl.append(leter)
                else:
                    costf += cost[index]
            else:
                stackl.append(leter)
                stackp.append(cost[index])
        return costf

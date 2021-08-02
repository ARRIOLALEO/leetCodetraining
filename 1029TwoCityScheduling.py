class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diference ={}
        for cost in costs:
            dif = abs(cost[0] - cost[1])
            if dif in diference:
                diference[dif] = diference[dif] + [cost]
            else :
                diference[dif] = [cost]
        sorted_dif = sorted(diference,key=lambda x:x,reverse=True)
        half = len(costs) // 2
        a , b = half,half
        solution = 0
        for dif in sorted_dif:
            element = diference[dif]
            for cost in element:
                if cost[0] < cost [1]:
                    if a > 0:
                        solution += cost[0]
                        a -= 1
                    else:
                        solution += cost[1]
                        b -= 1
                else:
                    if b > 0:
                        solution += cost[1]
                        b -= 1
                    else:
                        solution += cost[0]
                        a -= 1
        return solution

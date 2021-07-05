class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        solution = []
        intervals.sort()
        previus = intervals[0]
        for i in range(1,len(intervals)):
            if  intervals[i][0] <= previus[1] and intervals[i][1] >= previus[0]:
                limit_sup = intervals[i][1] if intervals[i][1] >= previus[1] else previus[1]
                limit_inf = intervals[i][0] if intervals[i][0] <= previus[0] else previus[0]
                previus = [limit_inf, limit_sup]
            else:
                solution.append(previus)
                previus =  intervals[i]
        solution.append(previus)       
        return solution

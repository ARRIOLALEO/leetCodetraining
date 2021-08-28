class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        dc = {}
        solution = [0] * k
        for t in logs:
            id = t[0]
            time =t[1]
            if id in dc:
                dc[id].add(time)
            else:
                dc[id] = set([time])
                
        for user in dc:
            id = len(dc[user])
            solution[id -1] +=1
        return solution
        
        

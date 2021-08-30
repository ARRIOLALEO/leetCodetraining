class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        if n == 0:
            return len(tasks)
        dc = {}
        for t in tasks:
            if t in dc:
                dc[t] += 1
            else:
                dc[t] = 1
        result =[]
        counter  = 0
        dc = dict(sorted(dc.items(),key=lambda item:item[-1]))
        dc  = dict(reversed(dc.items()))
        mx_f = list(dc.values())[0]
        x = []
        for i in dc:
            if dc[i] == mx_f:
                x += [i]
        return max(len(tasks),(mx_f - 1) * (n + 1) + len(x))

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        totals = {}
        solution = []
        for index,row in enumerate(mat):
            totals[index] = sum(row)
        total = dict(sorted(totals.items(), key = lambda item:item[1]))
        for ro in total:
                solution.append(ro)
        return solution[0:k]

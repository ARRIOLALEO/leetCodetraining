class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        solution = set()
        
        def backtracking(strg, nowSecuence, solution):
            if nowSecuence not in solution:
                solution.add(nowSecuence)
                if len(nowSecuence) == len(tiles):
                    return
                for i in range(len(strg)):
                    backtracking(strg[:i]+ strg[i+1:],nowSecuence + strg[i], solution)
            else:
                return
        backtracking(tiles,"",solution)
        return len(solution) -1

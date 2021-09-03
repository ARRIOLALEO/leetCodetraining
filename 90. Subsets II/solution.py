class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        W = len(nums)
        solution = [[]]
        nums.sort()
        for number in nums:
            solution += [cur + [number] for cur in solution]
        dc = {}
        solution2 = []
        for e in solution:
            x = [str(a) for a in e]
            x = "".join(x)
            if x in dc:
                pass
            else:
                dc[x] = 1
                solution2 += [e]
                
        return solution2

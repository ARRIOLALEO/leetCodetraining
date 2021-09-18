class Solution(object):
    def processQueries(self, queries, m):
        """
        :type queries: List[int]
        :type m: int
        :rtype: List[int]
        """
        p = []
        solution = []
        for i in range(1,m+1):
            p.append(i)
        for n in queries:
            position = p.index(n)
            solution.append(position)
            removed = p.pop(position)
            p = [removed] + p

        
        return solution

// Photo by Fakurian Design on Unsplash

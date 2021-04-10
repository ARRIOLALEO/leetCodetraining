class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        theGreates = max(candies)
        solution =[]
        for kid in candies:
            withExtraCandies = kid + extraCandies
            if withExtraCandies >= theGreates:
                solution.append(True)
            else:
                solution.append(False)
        return solution
        

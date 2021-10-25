class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        solution =0
        left, right = 0,len(people) -1
        people.sort()
        while left <= right:
            solution +=1
            if people[left] + people[right] <= limit:
                left +=1
            right -=1
        return solution

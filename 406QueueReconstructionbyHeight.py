class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people = sorted(people, key = lambda x:(-x[0],x[1]))
        
        for cur in range(len(people)):
            position = people[cur][1]
            if position < cur:
                person = people.pop(cur)
                people.insert(position,person)
            
        return people

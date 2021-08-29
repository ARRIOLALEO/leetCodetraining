class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:        
        groups = []
        dc = {}
        
        for index,id in enumerate(groupSizes):
            dc[index] = id
        dc = dict(sorted(dc.items(), key=lambda item:item[1]))
        
        groups = []
        temp = []
        
        for id in dc:
            temp.append(id)
            if dc[id] == len(temp):
                groups.append(temp)
                temp = []
        return groups
            

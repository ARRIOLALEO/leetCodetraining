class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        roots = {}
        for element in paths:
            split = element.split(" ")
            for i in range(1,len(split)):
                file = split[i]
                roots[file[file.index("(") + 1 :file.index(")")]] = []
        
        for element in paths:
            split = element.split(" ")
            root = split[0]
            for i in range(1,len(split)):
                file = split[i]
                content = file[file.index("(") + 1: file.index(")")]
                
                roots[content] = roots[content] + [root,file[0:file.index("(")]]
        solution = []
        for root in roots:
            parcial =[]
            if len(roots[root]) > 2:
                for i in range(0,len(roots[root]),2):
                    parcial.append(roots[root][i]+"/"+roots[root][i+1])
                solution.append(parcial)
        return solution
                

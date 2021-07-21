class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dct = {}
        for i in range(len(s)):
            if s[i] not in dct:
                dct[s[i]] = [i,i]
            else:
                dct[s[i]][1] = i
        
        parcials =[]
        temp = []
        for element in (dct):
            if (len(temp) == 0):
                temp = dct[element]
            elif temp[1] > dct[element][0]:
                if temp[1] < dct[element][1]:
                    temp[1] = dct[element][1]
            else:
                parcials.append(temp)
                temp = dct[element]
        parcials += [temp]
        solution = []
        
        for par  in parcials:
            solution.append(abs(par[1] - par[0]) + 1)
        return solution
#         i need to get the first and the last postion of the element
#         join all the elements that are in range 

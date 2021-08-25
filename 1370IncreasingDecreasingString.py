class Solution:
    def sortString(self, s: str) -> str:
        result = ""
        dtc = {}
        for i in s:
            dtc[i] = dtc.get(i,0) + 1
        
        reverse = False
        
        while dtc:
            for i in dict(sorted(dtc.items(),reverse = reverse)):
                result += i
                dtc[i] -= 1
                
                if not dtc[i]:
                    del dtc[i]
                    
            reverse = not reverse
            
        return result

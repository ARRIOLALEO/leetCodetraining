class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        hashtable ={}
        for atom in range(10,len(s)+1):
            temps = s[atom-10:atom]
            if temps in hashtable:
                hashtable[temps] +=1
            else:
                hashtable[temps] = 1
        solution = []
        for atom in hashtable:
            if hashtable[atom] > 1:
                solution.append(atom)
        return solution

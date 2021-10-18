class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        # create the base case
        solution = [s.lower()]
        
        # createing the backtracking interation 
        for i in range(len(s)-1,-1,-1):
            # is the element is alphanumeric we iterate the two options
            if s[i].isalpha():
                #create our new solution
                temp = []
                #iterate our previous solutions to create the new permutations
                for p in solution:
                    # adding previous permutations
                    temp.append(p)
                    #creating new permuatitions strings are inutable changing to list
                    p = list(p)
                    #change to uppercase our alpha character
                    p[i] = p[i].upper()
                    #add our permuation to solutions as str
                    temp.append("".join(p))
                #adding our new permutations to solutions
                solution = temp
        return solution

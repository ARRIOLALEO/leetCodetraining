class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        word = ""
        solution = []
        s = searchWord
        maxi = 3
        for i in s:
            word += i
            temp = []
            counter = 0
            while len(temp) < maxi and counter < len(products):
                if products[counter][0:len(word)] == word:
                    temp.append(products[counter])
                counter += 1
             if len(temp) < maxi:
                maxi = temp
            solution.append(temp)
        return solution
      
      # using a maxi as the max number of result if we have alredy some a previus result of 2 we dont need to iterate till the end of the array we 
      # just get less that makes the ALGO 10 faster
   class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        word = ""
        solution = []
        s = searchWord
        maxi = 3
        for i in s:
            word += i
            temp = []
            counter = 0
            while len(temp) < maxi and counter < len(products):
                if products[counter][0:len(word)] == word:
                    temp.append(products[counter])
                counter += 1
            if len(temp) < maxi:
                maxi = len(temp)
            solution.append(temp)
        return solution
         
            
            
            
        

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        values = set(arr)
        size = len(arr)
        dictionary = {}
        
        for number in arr:
            if number in dictionary:
                dictionary[number] +=1
            else:
                dictionary[number] =1
                
        half = size // 2
        
        multiples = []
        for element in dictionary:
            multiples.append(dictionary[element])
            
        multiples.sort(reverse=True)
        
        response = 0
        acc = 0
        for n in multiples:
            response +=1
            acc += n
            if acc >= half:
                return response
        
            

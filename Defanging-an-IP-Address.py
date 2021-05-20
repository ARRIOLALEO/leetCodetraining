class Solution:
    def defangIPaddr(self, address: str) -> str:
        solution = ""
        for element in address:
            if element == ".":
                solution +="[.]"
            else:
                solution += element
        return solution
        
#  class Solution:
#     def defangIPaddr(self, address: str) -> str:
#         return address.replace(".","[.]")

class ProductOfNumbers:

    def __init__(self):
        self.array = [1]
        

    def add(self, num: int) -> None:
        if num == 0:
            self.array = [1]
        else:
            self.array.append(num * self.array[len(self.array) -1] )
        return
        

    def getProduct(self, k: int) -> int:
        lent = len(self.array)
        if k < lent:
            return self.array[lent - 1]//self.array[lent - 1 - k]
        else:
            return 0
        

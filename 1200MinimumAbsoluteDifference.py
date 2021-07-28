class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        mini_dif = arr[1] - arr[0]
        solution =[]
        for i in range(2,len(arr)):
            mini_dif = min(abs(arr[i] - arr[i-1]) ,mini_dif)
        prev = arr[0]
        for i in range(1,len(arr)):
                if abs(arr[i] - prev) == mini_dif:
                    solution.append([prev,arr[i]])
                prev = arr[i]
                
        return solution

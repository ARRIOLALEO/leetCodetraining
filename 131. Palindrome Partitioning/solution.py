class Solution(object):
    def __init__(self):
        self.solution = []
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def dfs(cur_s, path_s):
            if not cur_s:
                self.solution.append(path_s)
                return 
            else:
                for index in range(1, len(cur_s) + 1):
                    if cur_s[:index] == cur_s[:index][::-1]:
                        dfs(cur_s[index:],path_s+[cur_s[:index]])
        dfs(s,[])
        return self.solution
        

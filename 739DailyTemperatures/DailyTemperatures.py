class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        T = temperatures
        
        ans = [0] * len(T)
        for i , t in enumerate(T):
            while st and t > T[st[-1]]:
                x = st.pop(-1)
                ans[x] = i - x
            st.append(i)
        return ans
        

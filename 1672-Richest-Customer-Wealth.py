class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxWealth = 0;
        for x in range(len(accounts)):
            maxWealth = max(maxWealth ,sum(accounts[x]))
        return maxWealth

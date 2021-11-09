class Solution:
    def canJump(self, nums: List[int]) -> bool:
        actual_position = [0]
        exist_position = set()
        goal = len(nums) -1
        while actual_position:
            position = actual_position.pop()
            jump = nums[position]
            for i in range(jump+1):
                if nums[position + i] == 0:
                    pass
                
                next_position = position + i
                if next_position == goal:
                    return True
                elif next_position not in exist_position:
                    actual_position.append(next_position)
                    exist_position.add(next_position)
                

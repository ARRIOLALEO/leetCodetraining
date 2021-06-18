def gravity(box):
    for row in range(len(box)):
        empty_position = 0
        for col in range(len(box[row])):
            col_position = len(box[row]) - col - 1
            is_stone = box[row][col_position]
            if is_stone == '#':
                [box[row][col_position], box[row][col_position
                 + empty_position]] = [box[row][col_position
                        + empty_position], box[row][col_position]]
            elif is_stone == '*':
                empty_position = 0
            elif is_stone == '.':
                empty_position = empty_position + 1
    return box

def flip(box):
    result = []
    for col in range(len(box[0])):
        result.append([])
        for row in range(len(box)):
            result[col].append(box[len(box) - row - 1][col])
    return result
    
class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        box = gravity(box)
        return(flip(box))
        

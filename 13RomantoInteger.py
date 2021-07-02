class Solution:
    def romanToInt(self, s: str) -> int:
        roman =["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        cipher=[1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        
        integer = 0
        pointer = 0
        while len(s) > 0:
            subs = 1 if (pointer % 2) == 0 else 2
            rm = s[0:subs]
            if rm == roman[pointer]:
                integer += cipher[pointer]
                s = s[subs: len(s) ]
            else:
                pointer += 1
        return integer

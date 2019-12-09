class Solution:
    def romanToInt(self, s: str) -> int:

        romanDict = {'I': 1 , 'V': 5 , 'X':10, 'L':50 , 'C':100, 'D':500 , 'M':1000}
        sum = 0
        romanList = list(s)

        for i , roman in enumerate(romanList):
            if i < len(romanList)-1:
                if romanDict[roman] < romanDict[romanList[i+1]] :
                    sum -= romanDict[roman]
                else :
                    sum += romanDict[roman]
            else :
               sum += romanDict[roman]

        return sum
        

class Solution:
    def reverse(self, x: int) -> int:
        reversedStringNum  =''.join(list(str(x))[len(list(str(x)))::-1])

        if reversedStringNum[-1] == '-':
            reversedInt = int(reversedStringNum[-1]+ reversedStringNum[0:-1])
            if (reversedInt > -2147483647) :
                return reversedInt
            else :
                return 0
        else :
            reversedInt = int(reversedStringNum)
            if (reversedInt < 2147483647) :
                return reversedInt
            else :
                return 0


        

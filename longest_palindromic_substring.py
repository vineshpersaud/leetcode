class Solution:
    def longestPalindrome(self, s: str) -> str:
        stringList = list(s)
        longestPalindrome = []

        for i, letter in enumerate(stringList):
            lastLetter = None
            noPal = True
            while len(stringList[i:lastLetter]) >= 1: 
                if stringList[i:lastLetter] == stringList[i:lastLetter][::-1] and len(stringList[i:lastLetter]) > len(longestPalindrome):
                    longestPalindrome = stringList[i:lastLetter]
                if lastLetter == None :
                    lastLetter = -1
                else:
                    lastLetter -= 1
        return(''.join(longestPalindrome))
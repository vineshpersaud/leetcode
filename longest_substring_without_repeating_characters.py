class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        strList = list(s)
        highestWord = []
        currentWord = []
        startingIndex = 0

        while startingIndex <= len(strList):
            for letter in strList[startingIndex:]:
                if currentWord == []:
                    currentWord.append(letter)
                    if len(currentWord) > len(highestWord):
                     highestWord = currentWord
                elif currentWord.count(letter) < 1:
                    currentWord.append(letter)
                elif currentWord.count(letter) >= 1:
                    if len(currentWord) > len(highestWord):
                        highestWord = currentWord
                    currentWord = []
                    break
                elif len(currentWord) > len(highestWord):
                    highestWord = currentWord
                    currentWord = []
            startingIndex +=1
        return len(highestWord)

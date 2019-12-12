class Solution:
    def isValid(self, s: str) -> bool:
        valid = True
        l = list(s)
        parDict = {'{':0 , '(':0 , '[':0 , ']':0 , ')':0 , '}':0 }
        
        for par in l :
            parDict[par] += 1
        
        if parDict['{'] != parDict['}'] :
            valid = False
        if parDict['('] != parDict[')'] :
            valid = False
        if parDict['['] != parDict[']'] :
            valid = False
        
        if len(l) >= 1  :
            if l[0] in [']','}',')'] :
                valid = False
            elif len(l) == 1:
                valid = False
            elif l[-1] in ['[','{','(']:
                valid = False

       
        if valid == True :
            for i,par in enumerate(l):
                if len(l) > i-1 :
                    if par == '(' and l[i+1] in ['}',']'] :
                        valid = False
                    elif par == '{' and l[i+1] in [')',']'] :
                        valid = False
                    elif par == '[' and l[i+1] in ['}',')'] :
                        valid = False
        for i, par in enumerate(l) :
            if i >= 1 and i < len(l)-2:
                if l[i-1] == '[' and l[i+1] == ']' and par in ['{','}','(',')']:
                    valid = False
                if l[i-1] == '{' and l[i+1] == '}' and par in ['[',']','(',')']:
                    valid = False
                if l[i-1] == '(' and l[i+1] == ')' and par in ['[',']','{','}'] :
                    valid = False

        return valid
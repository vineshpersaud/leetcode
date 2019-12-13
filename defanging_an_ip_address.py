class Solution:
    def defangIPaddr(self, address: str) -> str:
       return ''.join(list(map(lambda num: '[.]' if (num == '.') else num,address) ))
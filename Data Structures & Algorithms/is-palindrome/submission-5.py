class Solution:
    def isPalindrome(self, s: str) -> bool:

        newString = ""
        for c in s:
            if self.alNum(c):
                newString += c.lower()

        return newString == newString[::-1]

    

    def alNum(self, c: str) -> bool:
        return ((ord('A') <= ord(c) <= ord('Z')) or
                (ord('a') <= ord(c) <= ord('z')) or
                (ord('0') <= ord(c) <= ord('9')))
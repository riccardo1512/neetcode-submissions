class Solution:
    def isPalindrome(self, s: str) -> bool:

        i = 0
        j = len(s) - 1

        while i <= j:

            while i < j and not self.alphaNum(s[i]):
                i += 1
            while j > i and not self.alphaNum(s[j]):
                j -= 1

            if s[i].lower() != s[j].lower():
                return False
            
            i += 1
            j -= 1
        
        return True
    

    def alphaNum(self, c: char) -> bool:

        return ((ord('a') <= ord(c) <= ord('z')) or
                (ord('A') <= ord(c) <= ord('Z')) or
                (ord('0') <= ord(c) <= ord('9')))
        
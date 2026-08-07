class Solution:

    def encode(self, strs: List[str]) -> str:

        output = ""

        for s in strs:
            output += str(len(s)) + "#"
            output += s

        return output

    def decode(self, s: str) -> List[str]:
        
        output = []
        count = 0

        i = 0

        num = ""

        while i < len(s):

            if s[i].isdigit():
                num += s[i]
            
            if s[i] == '#':

                i += 1

                output.append("")
                
                for j in range(int(num)):
                    output[count] += s[i]
                    i += 1
                
                count += 1
                num = ""
            else:
                i += 1

        return output
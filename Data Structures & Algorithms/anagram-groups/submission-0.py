class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        sorted_list = []

        for i in range(len(strs)):
            sorted_list.append(''.join(sorted(strs[i])))

        
        d = {}

        output = []

        counter = 0

        for i in range(len(sorted_list)):

            if sorted_list[i] in d:
                output[d[sorted_list[i]]].append(strs[i])
            
            else:
                d.update({sorted_list[i] : counter})
                output.append([strs[i]])
                counter += 1


        return output

        
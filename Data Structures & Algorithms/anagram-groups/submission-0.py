from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       

        
        dict_strs= defaultdict(list)
        
        for every_str in strs:
            str_count=26*[0]
            for letter in every_str:
                str_count[ord(letter) - ord('a')]+=1

            tuple_str= tuple(str_count)
            
            dict_strs[tuple_str].append(every_str)

        return list(dict_strs.values())
        
        
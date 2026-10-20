class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        

        Counts, CountT ={},{}
        
        for i in range(len(s)):

            Counts[s[i]]= 1 + Counts.get(s[i],0)
            CountT[t[i]]= 1 + CountT.get(t[i],0)

        return Counts == CountT
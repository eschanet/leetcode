class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        while strs:
            s = strs.pop()
            print(s)
            if str(sorted(s)) in anagrams:
                anagrams[str(sorted(s))].append(s)
            else:
                anagrams[str(sorted(s))] = [s]
        
        ans = []
        for key, l in anagrams.items():
            ans.append(l)
        
        return ans
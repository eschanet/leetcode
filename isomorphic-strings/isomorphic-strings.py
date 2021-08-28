class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        map_s_t, map_t_s = {}, {}
        
        for idx in range(len(s)):
            if (
                not s[idx] in map_s_t
                and not t[idx] in map_t_s
            ):
                map_s_t[s[idx]] = t[idx]
                map_t_s[t[idx]] = s[idx]
            elif not (
                map_s_t.get(s[idx],None) == t[idx]
                and map_t_s.get(t[idx],None) == s[idx]
            ):
                return False
        
        return True
                
        
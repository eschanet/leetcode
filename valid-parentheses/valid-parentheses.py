class Solution:
    def isValid(self, s: str) -> bool:
        
        # quick sanity check before we deconstruct the string
        for o, c in [('(',')'), ('{','}'), ('[',']')]:
            if (s.count(o) + s.count(c)) % 2 != 0: return False
           
        import re
        replacements = {"\{\}": "", "\[\]": "", "\(\)": "",}
        pattern = re.compile("|".join(replacements.keys()))
        
        old, new = "", s
        while old != new:
            old = new
            new = pattern.sub(lambda m: replacements[re.escape(m.group(0))], old)
            
        if len(new) == 0: return True
        else: return False
class Solution:
    def isValid(self, s: str) -> bool:
                           
        old = ""
        while old != s:
            old = s
            s = s.replace('()','').replace('[]','').replace('{}','')
            
        if len(s) == 0: return True
        return False
    

    def isValid_regex(self, s: str) -> bool:
        
        import re
        replacements = {"\{\}": "", "\[\]": "", "\(\)": "",}
        pattern = re.compile("|".join(replacements.keys()))
        
        old = ""
        while old != s:
            old = s
            s = pattern.sub(lambda m: replacements[re.escape(m.group(0))], old)

        if len(s) == 0: return True
        return False
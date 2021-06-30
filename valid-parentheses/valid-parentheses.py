class Solution:
    def isValid_replacements(self, s: str) -> bool:       
        while '()' in s or '[]' in s or '{}' in s:
            s = s.replace('()','').replace('[]','').replace('{}','')            
        return s == ''

    def isValid_stack(self, s: str) -> bool:       
        stack = []
        hashmap = {
            ")":"(",
            "}":"{",
            "]":"[",
        }
        
        for c in s:
            if c in hashmap:
                if stack and stack[-1] == hashmap[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return len(stack) == 0

    def isValid(self, s: str) -> bool:
        return self.isValid_stack(s)

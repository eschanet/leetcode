class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digits_to_letters = {
            1 : [],
            2 : ['a','b','c'],
            3 : ['d','e','f'],
            4 : ['g','h','i'],
            5 : ['j','k','l'],
            6 : ['m','n','o'],
            7 : ['p','q','r', 's'],
            8 : ['t','u','v'],
            9 : ['w','x','y', 'z'],
            0 : [],
        }
        
        if len(digits) <= 0:
            return []
        
        # initialize with first letters
        combs = []
        for letter in digits_to_letters[int(digits[0])]:
            combs.append(letter)
            
        # create all remaining combinations
        for d in digits[1:]:
            current_combs = combs[:]
            for combination in current_combs:
                for letter in digits_to_letters[int(d)]:
                    combs.append(combination + letter)
                combs.pop(0)
                        
        return combs
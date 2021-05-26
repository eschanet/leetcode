class Solution:
    def trivial_fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for i in range(1,n+1):
            if (i % 15 == 0):
                answer.append("FizzBuzz")
            elif (i % 3 == 0):
                answer.append("Fizz")
            elif (i % 5 == 0):
                answer.append("Buzz")
            else:
                answer.append(str(i))
        return answer
        
    def fancy_fizzBuzz(self, n: int) -> List[str]:
        # FizzBuzz template
        tmplt = [None,None,"Fizz",None,"Buzz","Fizz",None,None,"Fizz","Buzz",None,"Fizz",None,None,"FizzBuzz"]
        
        # check how often we can fit template into n
        result = tmplt*(n // 15) + tmplt[0:(n % 15)] if n > 15 else tmplt[0:n]
        
        # map None to str integer by looking at index we are at
        return list(map(lambda e: e[1] if e[1] else str(e[0] + 1), enumerate(result)))
    
    
    def fizzBuzz(self, n: int) -> List[str]:
        return self.trivial_fizzBuzz(n)
        # return self.fancy_fizzBuzz(n)
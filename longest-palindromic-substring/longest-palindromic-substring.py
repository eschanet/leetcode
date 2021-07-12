class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def is_palindrome(s):
            return s == s[::-1]
        
        if is_palindrome(s): return s
        
        longest_palindrome = ""
        for i in range(len(s)):
            for j in range(len(s), -1 , -1):
                if i >= j-1:
                    continue
                if is_palindrome(s[i:j]):
                    if len(s[i:j]) > len(longest_palindrome):
                        longest_palindrome = s[i:j]
        
        if longest_palindrome == "":
            return s[0]
        
        return longest_palindrome
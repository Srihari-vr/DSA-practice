class Solution:
    def isPalindrome(self, a: str) -> bool:
        newstr=''
        for c in a:
            if c.isalnum():
                newstr+=c.lower()
        return newstr == newstr[::-1]
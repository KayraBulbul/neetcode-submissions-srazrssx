class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        output = ""

        for char in s:
            if char.isalnum():
                output += char

        return output == output[::-1]
"""
**LONGEST PALINDROMIC SUBSTRING**

 Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters."""


"#Solution"
def palindrome(x):
        if len(x) < 1:
                return False
        return x == x[:: -1]

def longestPalindrome(s:str):
        """
        :type s: str
        :rtype: str
        """
        y = len(s)
        x = []
        for i in range(y):
                for j in range(i+1, y):
                        b = s[i:j+1]
                        a = palindrome(b)
                        if a:
                                x.append(b)
                        else:
                                continue
        return x

# print(longestPalindrome('allen'))
        
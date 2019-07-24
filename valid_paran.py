"""
Given a string containing chars '(', ')', '{', '}', '[', ']'
determine if input string is valid

An input string if:
1. open bracket must be closed by same type of brackets
2. open bracket must be closed in the correct order

Input: "()"
Output: true

Input: "(]"
Output: false
"""

def _is_valid(s):

     mapping = {'}': '{', ')': '(' , ']': '['}
     stack = []
     for char in s:
         if char in mapping.values():
             stack.append(char)
         elif char in mapping.keys():
             if stack == [] or mapping[char] != stack.pop():
                 return False
         else:
             return False
     return stack == []

if __name__=="__main__":
    print(_is_valid("()"))
    print(_is_valid("(]"))






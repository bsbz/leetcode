"""
Given a string S of '(' and ')' parentheses, we add the minimum number of parentheses ( '(' or ')', 
and in any positions ) so that the resulting parentheses string is valid.

Formally, a parentheses string is valid if and only if:

    It is the empty string, or
    It can be written as AB (A concatenated with B), where A and B are valid strings, or
    It can be written as (A), where A is a valid string.

Given a parentheses string, return the minimum number of parentheses we must add to make the resulting string valid.

Example 1:

Input: "())"
Output: 1

Example 2:

Input: "((("
Output: 3
"""

def minAddToMakeValid(S):        
        st = []
        result = []
        
        for c in S:
            if c == "(":
                st.append(c)               
            elif st == []:
                result.append(c)
            else:
                st.pop()
                
        return len(st) + len(result)


S = "())"
print(minAddToMakeValid(S))

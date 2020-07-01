"""
Given a string s. You should re-order the string using the following algorithm:

    Pick the smallest character from s and append it to the result.
    Pick the smallest character from s which is greater than the last appended character to the result and append it.
    Repeat step 2 until you cannot pick more characters.
    Pick the largest character from s and append it to the result.
    Pick the largest character from s which is smaller than the last appended character to the result and append it.
    Repeat step 5 until you cannot pick more characters.
    Repeat the steps from 1 to 6 until you pick all characters from s.

In each step, If the smallest or the largest character appears more than once you can choose any occurrence and append it to the result.

Return the result string after sorting s with this algorithm.

 

Example 1:

Input: s = "aaaabbbbcccc"
Output: "abccbaabccba"
Explanation: After steps 1, 2 and 3 of the first iteration, result = "abc"
After steps 4, 5 and 6 of the first iteration, result = "abccba"
First iteration is done. Now s = "aabbcc" and we go back to step 1
After steps 1, 2 and 3 of the second iteration, result = "abccbaabc"
After steps 4, 5 and 6 of the second iteration, result = "abccbaabccba"
"""

from collections import Counter
from string import ascii_lowercase

def sortString(s):
        result = []
        c = Counter(s)
             
        while len(result) < len(s):  
            # increasing order (a-z)
            for i in ascii_lowercase:
                if c[i] > 0:
                    result.append(i)
                    c[i] -= 1
            # decreasing order (z-a)
            for i in ascii_lowercase[::-1]:
                if c[i] > 0:
                    result.append(i)
                    c[i] -= 1
                                 
        return ''.join(result)

s = "aaaabbbbcccc"
print(sortString(s)) 



'''

All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, 
it is sometimes useful to identify repeated sequences within the DNA.
Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

Example:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC", "CCCCCAAAAA"]

'''

def findRepeatedDnaSequences(s):

        result = []
        d = {}
        
        for i in range(len(s)):
            if s[i:i+10] not in d:
                d[s[i:i+10]] = 1
            else:
                d[s[i:i+10]] += 1
                result.append(s[i:i+10])

        return set(result)

s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTTAAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
problem = findRepeatedDnaSequences(s)
print(problem)

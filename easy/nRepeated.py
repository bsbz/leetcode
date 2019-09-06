'''
In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.

Return the element repeated N times.

Example 1:

Input: [1,2,3,3]
Output: 3
'''

def repeatedNTimes(A):
    """
    :type A: List[int]
    :rtype: int
     """

    for i in range(len(A)):
        for j in range(i):
            if A[i] == A[j]:
                return A[i]

arr = [1,2,3,3]

res = repeatedNTimes(arr)
print(res)            

'''
        Given an array of integers A sorted in non-decreasing order, return an array 
        of the squares of each number, also in sorted non-decreasing order.

        Example 1:

        Input: [-4,-1,0,3,10]
        Output: [0,1,9,16,100]
'''

def sortedSquares(A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        """
        squares = []
        for item in A:
            squares.append(item*item)
        return sorted(squares)
        """
        
        for i in range(len(A)):
            A[i] **= 2
        return sorted(A)

arr = [-4,-1,0,3,10]

res = sortedSquares(arr)
print(res)

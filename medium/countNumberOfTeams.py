'''
    There are n soldiers standing in a line. Each soldier is assigned a unique rating value.
    You have to form a team of 3 soldiers amongst them under the following rules:

        - Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
        - A team is valid if:  (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).

    Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).

    Example 1:

    Input: rating = [2,5,3,4,1]
    Output: 3
    Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1). 

'''

def numTeams(rating):
        #print(rating)
        count = 0
        
        for i in range(len(rating)):
            for j in range(i+1, len(rating)):
                for k in range(j+1, len(rating)):
                    if (rating[i] > rating[j] > rating[k]) or (rating[i] < rating[j] < rating[k]):
                        count += 1
        return count

input = [3,2,4,5,1,8,6,9,7]
print(numTeams(input))

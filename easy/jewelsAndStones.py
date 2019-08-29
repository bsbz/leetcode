def numJewelsInStones(J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count = 0
        setJ = set(S)
        for jewel in S:
            if jewel in J:
                count += 1
        return count

J = "aA"
S = "aAAbbbb"
res = numJewelsInStones(J, S)
print(res)

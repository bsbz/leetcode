def removeOuterParentheses(S: str) -> str:
    cnt = 0
    res = []
        
    for c in S:
        if c == '(':
            cnt +=1
            if cnt > 1:
                res.append(c)
        else:
            cnt -= 1
            if cnt != 0:
                res.append(c)
    return ''.join(res)    

s = "(()())(())(()(()))"

res = removeOuterParentheses(s)
print(res)

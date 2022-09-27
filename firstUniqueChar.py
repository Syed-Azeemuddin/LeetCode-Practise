# def uniqChar(s):
    # charList = list(s)
    # l = list(set(s)) 

    # for i in charList:
    #     if l[0] == i:
    #         return charList.index(str(i))
    #     else:
    #         return -1

def uniqChar(s):
    s = list(s)
    l = 0
    r = len(s) - 1

    while l <= r:
        
        if s[l] == s[r]:
            l += 1
            r = len(s) - 1
        else:
            r -= 1

        if l == r and s[l] != s[l-1]:
            return l
        
    return -1
        


print(uniqChar("abab"))



    
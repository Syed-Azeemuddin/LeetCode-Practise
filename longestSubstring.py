class Solution:

    def longSubstring(self, s: str):

        m = {}
        l = 0
        r = 0
        n = len(s) 
        

        ans = 0

        while(l < n and r < n):
            el = s[r]

            if(el in m):
                l= max(l, m[el] + 1)

            m[el] = r
            ans = max (ans, r-l+1)
            r += 1

        return ans


b = Solution()

answ = b.longSubstring("abababacade")
print(answ)

#{0,1,}
#"abababacade"
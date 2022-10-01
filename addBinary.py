class Solution(object):

    def addBinary(self, a, b):
        """
        TimeO = O(N) {iterating through the big len(str)}
        SpaceO = O(N) {using a list to store}
        """

        i,j = len(a)-1, len(b)-1
        c = 0
        result = []

        while i>=0 or j>=0 or c:
            total = c

            if i>=0:
                total += int(a[i])
                i-=1
            if j>=0:
                total += int(b[j])
                j-=1
            result.append(str(total%2))
            c = total//2
        return ''.join(reversed(result))
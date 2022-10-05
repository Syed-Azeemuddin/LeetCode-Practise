from typing import List


class Solution(object):

    def findHash(self,i):
        return "".join(sorted(i))

    def groupAnagram(self, arr:List[str])->List[List[str]]:

        m = {}
        ls = []

        for i in arr:
            hash = self.findHash(i)
            if hash not in m:
                m[hash] = []
            m[hash].append(i)
        
        for p in m.values():
            ls.append(p)
        
        return ls

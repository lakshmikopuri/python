#First Unique Character in a String
#Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
class Solution:
    def firstUniqChar(self, s: str) -> int:
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for index, char in enumerate(s):
            if d[char] == 1:
                return index

        return -1 

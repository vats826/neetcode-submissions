class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        arr = [0]*26
        for char in s:
            arr[ord(char)-ord('a')]+=1
        for char in t:
            arr[ord(char)-ord('a')]-=1
        return all(x==0 for x in arr)
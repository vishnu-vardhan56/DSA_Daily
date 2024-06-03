class Solution:
    def reverseVowels(self, s: str) -> str:
        ov = ['a','e','i','o','u','A','E','I','O','U']
        s = list(s)
        rev = []
        i = 0
        j = len(s) - 1
        while(i<j):
            if(s[i] in ov and s[j] in ov):
                s[i], s[j] = s[j] , s[i]
                i = i + 1
                j = j - 1
            elif (s[i] not in ov):
                i = i + 1
            elif (s[j] not in ov):
                j = j - 1
        return "".join(s)

        
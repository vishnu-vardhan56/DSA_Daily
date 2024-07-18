class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Method 1
        # l1 = list(s)
        # l2 = list(t)
        # if sorted(l1) == sorted(l2):
        #     return True
        # return False

        #Method 2 
        return Counter(s) == Counter(t)

        
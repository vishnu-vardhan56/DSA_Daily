class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if(len(words) != len(pattern)):
            return False
        d = {}
        uniq = set()
        for i in range(len(words)):
            if pattern[i] in d:
                if d[pattern[i]] != words[i]:
                    return False
            else:
                if words[i] not in uniq:
                    d[pattern[i]] = words[i]
                    uniq.add(words[i])
                else:
                    return False
        # keys = list(d.keys())
        # for i in range(len(keys)):
        #     for j in range(i+1,len(keys)):
        #         if d[keys[i]] == d[keys[j]]:
        #             return False
        return True
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = Counter(list(s))
        t_count = Counter(list(t))

        if len(s_count.keys()) >= len(t_count.keys()):
            longest = s_count
        else:
            longest = t_count

        for key in longest.keys():
            if not s_count[key] == t_count[key]:
                return False
        return True
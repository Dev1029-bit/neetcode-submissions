class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = {}
        for i in range(len(strs)):
            rev_str = "".join(sorted(strs[i]))
            lst = []
            if rev_str in freq:
                freq[rev_str].append(strs[i])
            else:
                lst.append(strs[i])
                freq[rev_str] = lst
        return list(freq.values())





        
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res_map = {}

        for st in strs:
            str_map = {}
            for c in st:
                if c not in str_map:
                    str_map[c] = 1
                else:
                    str_map[c] += 1
            str_key = str(sorted(str_map.items()))
            if str_key in res_map:
                res_map[str_key].append(st)
            else:
                res_map[str_key] = [st]
        return list(res_map.values())
        
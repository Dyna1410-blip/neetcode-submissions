class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dd = defaultdict(list)
        for s in strs:
            code = [0] * 26
            for let in s:
                code[ord(let)-ord('a')] += 1
            dd[tuple(code)].append(s)
        return list(dd.values())


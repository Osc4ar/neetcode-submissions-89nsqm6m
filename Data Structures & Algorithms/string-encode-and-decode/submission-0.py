class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''

        for s in strs:
            s_len = str(len(s)) + '_'
            encoded += s_len
            encoded += s

        return encoded

    def decode(self, s: str) -> List[str]:
        strs = []

        i = 0
        while i < len(s):
            size = ''
            while s[i] != '_':
                size += s[i]
                i += 1

            start = i + 1
            end = start + int(size)
            strs.append(s[start:end])
            i = end
        
        return strs
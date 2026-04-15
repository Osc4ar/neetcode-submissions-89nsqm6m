class Solution:

    # Use an encoding like this: 2#hi5#there
    def encode(self, strs: List[str]) -> str:
        encoded = ''

        for s in strs:
            encoded += str(len(s)) + '#' + s

        return encoded

    def decode(self, s: str) -> List[str]:
        i = 0
        strs = []

        while i < len(s):
            size = ''
            while s[i] != '#':
                size += s[i]
                i += 1

            i += 1
            strs.append(s[i:i+int(size)])
            i += int(size)

        return strs
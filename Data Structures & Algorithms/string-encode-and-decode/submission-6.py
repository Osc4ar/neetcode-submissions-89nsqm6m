class Solution:

    '''
    We can use '#' and the size of the strings to encode and
    to separate strings. But we may run into those characters in ASCII so the
    separator may be something else

    We need a way to identify when the size ends and a regular number starts
    We could use the _ as end of size.

    Do we even need the #? Probably we can just have {size}_{text} and assume that every number
    we are reading is a size, because we will jump between size specifications
    '''
    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for s in strs:
            encoded += f'{len(s)}_'
            encoded += s

        return encoded

    def decode(self, s: str) -> List[str]:
        print(s)
        decoded = []

        i = 0
        current_size = ''
        while i < len(s):
            c = s[i]

            if c.isdigit():
                current_size += c
                i += 1
            elif c == '_':
                size = int(current_size)
                decoded.append(s[i+1:i+size+1])
                i += size + 1
                current_size = ''
        
        return decoded 

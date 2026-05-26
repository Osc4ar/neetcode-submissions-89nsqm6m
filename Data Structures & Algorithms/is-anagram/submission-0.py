class Solution:
    '''
    Using frequency maps of how many times each letter appears in a given string
    we can compare if both frequency maps are the same.

    Building the frequency map has a Time Complexity of O(n) and a Memory Complexity of O(n).
    It would be faster than ordering the arrays and comparing them, because ordering would take
    O(n log(n)) in most cases.
    '''
    def isAnagram(self, s: str, t: str) -> bool:
        s_freq = self.getFrequencies(s)
        t_freq = self.getFrequencies(t)

        return s_freq == t_freq

    def getFrequencies(self, s: str) -> dict:
        frequencies = defaultdict(int)

        for c in s:
            frequencies[c] += 1

        return frequencies
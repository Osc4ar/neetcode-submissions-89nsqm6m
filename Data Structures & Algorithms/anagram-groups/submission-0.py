class Solution:
    '''
    We could group the anagrams by the frequency of each letter in a dictionary.

    Usually, the frequency could be saved in a dictionary itself, but in this case
    we may use something hashable like a tuple instead. We can have an array with
    26 positions and increase by 1 for every character:
     a  b  c  d       z
    [0, 0, 0, 0, ... ,0]

    The array can be converted to a Tuple to be hashable, in that way we group anagrams.

    To build the result we iterate the dictionary, we add to the result every group which is
    already stored a list of strings
    '''
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_by_frequencies = defaultdict(list)
        
        for s in strs:
            frequencies = self.getFrequency(s)
            strs_by_frequencies[frequencies].append(s)

        return [anagrams for anagrams in strs_by_frequencies.values()]             

    def getFrequency(self, s: str) -> Tuple[int]:
        frequencies = [0] * 26

        for c in s:
            position = ord(c) - ord('a')
            frequencies[position] += 1

        return tuple(frequencies)
class Solution:
    '''
    We can solve this problem by doing two different steps:
    * Identifying which parenthesis to remove
    * Removing the "marked" parenthesis

    1. Iterate over the string, keep a count of the parenthesis
    2. The count will start at 0, if we find any closing parenthesis we mark it with *
    3. If we find an opening parenthesis we increase the count by 1
    4. After doing this, we will have all extra closing parenthesis marked.
    5. If the count is bigger than zero at the end of the iteration, iterate the
       string in reverse, mark any opening parenthesis found with * and decrease the count
       until count is zero
    6. Remove all marked parenethesis from String and return the cleaned string

    We are iterating the array multiple times, but time complexity is O(n)
    Memory complexity is O(1) since we are only storing a count.
    '''
    def minRemoveToMakeValid(self, s: str) -> str:
        as_list = list(s)
        count = 0
        for i in range(len(as_list)):
            if as_list[i] == ')' and count == 0:
                as_list[i] = '*'
            elif as_list[i] == ')':
                count -= 1
            elif as_list[i] == '(':
                count += 1

        i = len(as_list) - 1
        while count > 0 and i >= 0:
            if as_list[i] == '(':
                as_list[i] = '*'
                count -= 1
            i -= 1

        cleaned = []
        for c in as_list:
            if c != '*':
                cleaned.append(c)

        return ''.join(cleaned)

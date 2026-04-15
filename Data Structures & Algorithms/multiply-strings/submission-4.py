class Solution:
    '''
    Wrong approach, more efficient for short numbers:
        We have to implement two things: str_to_int and int_to_str.
        Let's assume that the numbers we are parsing fit in a primitive type.

    The integers may not fit in a regular integer or BigInt type. We have to focus in the algorithm to multiply two big numbers and consider the carry.
    The max size of the result will be n+m. We can create an array to hold the value, iterate each number and sum its digits into the position.
    The position of a given operation is: i + j

    1. Create an array of size n+m with zero values.
    1a. Optionally convert the input strings into lists of int
    2. We will iterate the first array in reverse
    3. For each number, multiple the current digit by each of the second array digits
    4. Sum the result in the result array as follows:
        a. The value in the position i+j will be the module: result%10. The units of the product
        b. The value in the position i+j+1 will be the division: result/10 - It can be zero. The tents of the product
        Note: By having different position in the result array, we are considering the different powers of 10 of each digit 
    5. Once all digits are multiplied, reverse the list of numbers and convert it into a string
    '''
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'

        max_size = len(num1) + len(num2)
        result = [0] * max_size

        int_num1 = [int(c) for c in num1]
        int_num2 = [int(c) for c in num2]

        for i, digit1 in enumerate(reversed(int_num1)):
            for j, digit2 in enumerate(reversed(int_num2)):
                product = digit1 * digit2
                result[i+j] += product
                result[i+j+1] += result[i+j] // 10 # Integer division, might be zero
                result[i+j] = result[i+j] % 10

        # Remove the leading zeroes
        i = max_size - 1
        while result[i] == 0:
            i -= 1

        str_list_result = reversed([str(d) for d in result[:i+1]])
        return ''.join(str_list_result)

'''
String to atoi
1. discards whitespace characters
2. optional intital plus and minus sign
3. string can contain additional characters

Input: "42"
Output: 42

Input: "   -42"
Output: -42

Input: "4193 with words"
Output: 4193

Input: "words and 987"
Output: 0

Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Therefore INT_MIN (−231) is returned.
'''
INT_MAX = 2147483647
INT_MIN = -2147483648

class solution:

    def atoi(self, str):
        pointer = 0
        isNegative = False

        #loop
        while pointer<len(str) and str[pointer] == '':
            pointer  += 1

        # null condition
        if pointer == len(str):
            return 0

        # - or + sign set the flag
        if str[pointer] == '-':
            isNegative = True
            pointer += 1

        elif str[pointer] == '+':
            isNegative = False
            pointer += 1

        solution = 0
        for pointer in range(pointer, len(str)):
            # check if its numeric
            if not str[pointer].isdigit():
                break
            else:
                solution *= 10
                solution += int(str[pointer])

        # if no valid conversion is found
        if not isNegative and solution > INT_MAX:
            return INT_MAX
        elif isNegative and solution > INT_MAX:
            return INT_MIN

        if isNegative:
            return -1 * solution
        else:
            return solution




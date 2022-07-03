# String-to-Integer-atoi-
String to Integer (atoi)_python_leetcode_solution
class Solution:
    def myAtoi(self, s: str) -> int:
        number, sign = 0, 1
        # remove leading whitespace
        s = s.lstrip()
        # if string is empty, so return 0
        if not s: return 0
        # check minus charater
        if s[0] == "-":
            s = s[1:]
            sign = -1
        # check plus charater
        elif s[0] == "+":
            s = s[1:]
        # make foreach every charater
        for i in range(len(s)):
            if s[i] in "0123456789":
                number = number * 10 + int(s[i])
            else:
                break
        # check number is nol
        if number == 0: return 0
        # string converts to number
        number = sign * number
        int32_min, int32_max = -2**31, 2**31-1
        if number < int32_min: return int32_min
        if number > int32_max: return int32_max
        return number

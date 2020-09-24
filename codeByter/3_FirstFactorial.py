# Have the function FirstFactorial(num) take the num parameter being passed
# and return the factorial of it.
# For example: if num = 4, then your program should return (4 * 3 * 2 * 1) = 24.
# For the test cases, the range will be between 1 and 18 and the input will always be an integer.
# Examples
# Input: 4
# Output: 24
# Input: 8
# Output: 40320


def FirstFactorial(num):
    # code goes here
    num = int(num)
    if num == 1:
        return 1
        pass
    else:
        return num * FirstFactorial(num-1)
        pass


# keep this function call here
print(FirstFactorial(input()))

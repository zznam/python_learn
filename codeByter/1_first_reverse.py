# First Reverse
# Have the function FirstReverse(str) take the str parameter being passed
# and return the string in reversed order.
# For example: if the input string is "Hello World and Coders"
# then your program should return the string sredoC dna dlroW olleH.
# Examples
# Input: "coderbyte"
# Output: etybredoc
# Input: "I Love Code"
# Output: edoC evoL I


def FirstReverse(str):
    temp = ""
    for i in range(len(str)):
        temp = str[i] + temp
        pass
    # code goes here
    return temp


# keep this function call here
print(FirstReverse(input()))
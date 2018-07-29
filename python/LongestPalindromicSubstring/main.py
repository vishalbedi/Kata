

def longetst_Palindrome(input: str)-> str:
    if len(input) <= 1:
        return input
    longest_string = ""
    for i in range(len(input) + 1):
        len_odd = palendrome_length(input, i,i)
        len_even = palendrome_length(input, i, i+1)
        len_palindrome = max(len_odd, len_even)
        if len_palindrome > len(longest_string):
            p1 = i - int((len_palindrome -1)/2)
            p2 = i + int(len_palindrome/2)
            longest_string = input[p1:p2+1]
    return longest_string


def palendrome_length(input:str, left:int, right:int) -> int:
    while left >=0  and right < len(input) and input[left] == input[right]:
        left-=1
        right+=1
    return right - left - 1

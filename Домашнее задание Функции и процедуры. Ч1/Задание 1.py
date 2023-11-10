def is_palindrome(s):
    return s == s[::-1]

input_string = input()
print(is_palindrome(input_string))

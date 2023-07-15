#!/usr/bin/python3

def multiple_returns(sentence):
    length = len(sentence)
    first_char = sentence[0] if length > 0 else None
    return length, first_char

# Example usage:
sentence = "Hello, World!"
result_tuple = multiple_returns(sentence)
print(result_tuple)  # Output: (13, 'H')

empty_sentence = ""
result_tuple_empty = multiple_returns(empty_sentence)
print(result_tuple_empty)  # Output: (0, None)

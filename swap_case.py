"""
You are given a string and your task is to swap cases.
In other words, convert all lowercase letters to uppercase letters and vice versa.
"""


def swap_case(s):
    st = ""
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for c in s:
        if c in upper:
            st += c.lower()
        else:
            st += c.upper()
    return st


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
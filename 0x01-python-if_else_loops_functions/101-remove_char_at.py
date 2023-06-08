#!/usr/bin/python3
def remove_char_at(str, n):
    ans = ""
    for m in range(len(str)):
        if m != n:
            ans = ans + str[m]
    return (ans)

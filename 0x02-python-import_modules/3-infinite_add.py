#!/usr/bin/python3
if __name__ == "__main__":
    """add all arguments"""
    import sys

    answer = 0
    for m in range(len(sys.argv) - 1):
        answer += int(sys.argv[m + 1])
    print("{}".format(answer))

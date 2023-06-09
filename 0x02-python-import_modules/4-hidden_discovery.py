#!/usr/bin/python3

if __name__ == "__main__":
    """all names in compiled module"""
    import hidden_4

    answers = dir(hidden_4)
    for answer in answers:
        if answer[:2] != "__":
            print(answer)

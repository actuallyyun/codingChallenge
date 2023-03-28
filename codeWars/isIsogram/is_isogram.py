def is_isogram_1(string):
    return len(string)==set(string.lower())


def is_isogram_2(string):
    string=string.lower()
    for s in string:
        if string.count(s)>1:
            return False
    return True

def isP(s):

    strCleaned=[s.lower() for s in s if s.isalnum()]

    str1="".join(strCleaned)

    strCleaned.reverse()

    strReversed="".join(strCleaned)

    return str1==strReversed
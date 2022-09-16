def r_strlen(str):
    if str == '': return 0
    return 1 + r_strlen(str[1:])

# print(r_strlen('abcde'))
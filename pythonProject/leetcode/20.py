s = "()"
i = 0
j = 1
while i < len(s):
    if s[i] == "(" and s[j] == ")":
        i += 2
        j += 2
    elif s[i] == "[" and s[j] == "]":
        i += 2
        j += 2
    elif s[i] == "{" and s[j] == "}":
        i += 2
        j += 2
    else:
        print(False)
print(True)
# print(s[0] == s[1])
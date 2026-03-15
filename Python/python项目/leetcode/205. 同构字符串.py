# class Solution:

#     def isIsomorphic(self, s: str, t: str) -> bool:
#         ss = ""
#         if s < t:
#             for i in range(0, 26):
#                 for j in range(len(s)):
#                     ss[j] = chr(ord(s[j]) + i)
#                 if ss == t:
#                     break
#                 else:
#                     return False
#             return True
#         # elif s > t:
#         #     for i in range(0, 26):
#         #         for j in range(len(t)):
#         #             t[j] = chr(ord(s[j]) + i)
#         #         if s == t:
#         #             break
#         #         else:
#         #             return False
#         #     return True
#         # else:
#         #     return True


# Solution().isIsomorphic("bar", "foo")
s = "boo"
t = "faa"
ss = [""]*len(s)
if s < t:
    for i in range(0, 26):
        for j in range(len(s)):
            ss[j] = chr(ord(s[j]) + i)
        if ss == t:
            print(True)
            break

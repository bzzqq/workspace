class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        columnTitle = columnTitle[::-1]
        alphabet = [
            "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
            "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
        ]
        number = 0
        for i in range(len(columnTitle)):
            number = number + (alphabet.index(columnTitle[i]) + 1) * 26**i
        print(number)


columnTitle = "ZY"
print(columnTitle)
result = Solution()
result.titleToNumber(columnTitle)
# self = "zhangbin"
# Solution.titleToNumber(self, columnTitle)

columnNumber = 701
alphabet = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
]
result = []
while columnNumber > 0:
    columnNumber = columnNumber -1
    chr = alphabet[columnNumber % 26]
    result.append(chr)
    columnNumber = columnNumber // 26
result = "".join(result[::-1])
print(result)

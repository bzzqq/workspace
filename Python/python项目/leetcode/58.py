# 给你一个字符串 s，由若干单词组成，单词前后用一些空格字符隔开。返回字符串中最后一个单词的长度。
s = "Hello World"
s = s.rstrip()
s = s.split(" ")
print(len(s[-1]))
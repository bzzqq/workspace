import re

text = """style="line-height: 42px;"><div class="sname fl"><p style="line-height: 42px;">张斌</p><p class="num"></p></div> <span class="grade fr">89 points</span> <div class="clear"></div></div> <!----> <p class="dec"><!----> <span style="color: rgb(100, 104, 115);">能够对问题进行充分的分析，建立数学模型并使用适当的数学工具进行模型求解，但未对求解结果进行充分的分析和解释，论文存在格式错误。</span></p></div></dd></dl></div></li> <!----> <!----> <!----></ul> <!----></div></li></ul> <div class="page-container clearaft"><div class="left-box fl"><div class="user-info clearaft"><div class="fl left"><div """

matches = re.findall(r'><span*?</span>', text)

print(matches)

for match in matches:
    print(match)
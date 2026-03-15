import random

# 定义花色
suits = ["梅花", "红桃", "方块", "黑桃"]
# 定义牌面
numbers = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
# 定义牌型，拼接花色和牌面
poker_list = [suit + number for suit in suits for number in numbers]
# 增加大小王
poker_list.append("大王")
poker_list.append("小王")

# 生成三个玩家，每个玩家17张牌
player1 = []
player2 = []
player3 = []

# 将牌打乱顺序
random.shuffle(poker_list)
# 将牌分发给3个玩家
for i in range(17):
    player1.append(poker_list[i])
    player2.append(poker_list[i+17])
    player3.append(poker_list[i+17*2])

print("玩家1的牌是：", player1)
print("玩家2的牌是：", player2)
print("玩家3的牌是：", player3)
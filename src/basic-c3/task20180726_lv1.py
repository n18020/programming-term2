'''#関数定義
import random
s = 0   #出た目
g = 0   #進むマスの数
# 関数
def shake_dice():
    s = random.randint(1, 6)
    return s
def go_forward(g):
    g += s
    return g

while g < 10:
    enter = input("サイコロを振ってください。")
    if enter != "":
        continue
    s = shake_dice()
    g = go_forward(g)
    if g < 10:
        print("{}が出ました。現在位置{}はです。".format(s, g))
        continue
    break
print("{}が出ました。おめでとうございます、ゴールしました!".format(s))'''


goal_pos = 10
cur_x = 0
dice_num = 0

while cur_x

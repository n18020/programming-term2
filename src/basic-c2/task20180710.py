#必ず負けるじゃんけん
#入力される手
hand = input('何を出しますか？1:グー、2:チョキ、3:パー')

#プレイヤーが出した手
fmt = 'CPUが{your_hand}をだしました。あなたの負けです。'
if hand == str(1):
    s = fmt.format(your_hand = 'パー')
elif hand == str(2):
    s = fmt.format(your_hand = 'グー')
elif hand == str(3):
    s = fmt.format(your_hand = 'チョキ')
else:
    s = '入力が不正です。終了します。'

#出力結果
print(s)

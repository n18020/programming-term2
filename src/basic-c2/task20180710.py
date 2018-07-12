#必ず負けるじゃんけん
#入力される手
hand = input('何を出しますか？1:グー、2:チョキ、3:パー')

#プレイヤーが出した手
if hand == str(1):
    result = 'あなたはグー、CPUがパーをだしました。あなたの負けです。'
elif hand == str(2):
    result = 'あなたはチョキ、CPUがグーをだしました。あなたの負けです。'
elif hand == str(3):
    result = 'あなたはパー、CPUがチョキをだしました。あなたの負けです。'
else:
    result = '入力が不正です。終了します。'

#出力結果
print(result)

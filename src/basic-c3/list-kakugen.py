import random

#格言をリストに代入
kakugen = [
    '脳ある鷹は爪を隠す',
    '豚に真珠',
    '二兎を追うものは一兎をも得ず',
    '叩き続けなさい。そうすれば開かれます']
#ランダムに数値をひとつ選ぶ
i = random.randint(0, len(kakugen)-1)
print(kakugen[i])

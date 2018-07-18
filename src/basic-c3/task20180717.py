import random

constellation = [
      '牡羊座',
      '牡牛座',
      '双子座',
      '蟹座',
      '獅子座',
      '乙女座',
      '天秤座',
      '蠍座',
      '射手座',
      '山羊座',
      '水瓶座',
      '魚座']

fortune = [
      '良い',
      '悪い',
      '普通']

lucky_color = [
    '赤',
    '青',
    '緑',
    '紫',
    '黒',
    '黃',
    '橙']

fconstellation = random.randint(0, len(constellation) - 1)
ffortune = random.randint(0, len(fortune) - 1)
flucky_color = random.randint(0, len(lucky_color) - 1)
print('今日の{}の運勢は{}です。ラッキーカラーは{}。'.format(constellation[fconstellation], fortune[ffortune], lucky_color[flucky_color]))

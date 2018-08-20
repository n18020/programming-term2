import re

moji = input('全角カナの文字を入力してください\n')
pat = re.compile(r"[\u30A1-\u30F4]+")
if pat.fullmatch(moji):
    print(moji, 'は全角カナのみの文字列です')
else:
    print(moji, 'に全角カナ以外が含まれています')

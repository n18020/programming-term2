import re

url = input("URLを入力してください\n")

if re.match(r"^https|http\/\/", url):
    print(url, "はURLの形式です")
else:
    print(url, "はURLの形式ではありません")

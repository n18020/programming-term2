import re

file_name = input('テキスト形式のファイル名を入力してください\n')
pat = r"\.txt$"
if re.search(pat, file_name):
    print(file_name, 'は拡張子が.txtのテキストのファイルです')

else:
    print(file_name, 'は拡張子が.txtのテキストファイルではありません')

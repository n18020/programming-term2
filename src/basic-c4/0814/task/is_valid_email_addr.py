import re

mail_add = input("メールアドレスを入力してください\n")

mail = '^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$'
if re.search(mail, mail_add):
    print(mail_add, "はメールアドレス形式です")
else:
    print(mail_add, "はメールアドレス形式ではありません")

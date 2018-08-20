#テキストからキーワードを探す
key = 'find'
with open('mt7_7.txt', encoding='utf-8') as tf:
    #一行ずつファイルを読む
    for i, line in enumerate(tf):    #enumerate()関数を使う
        #文字列keyが行に含まれるか
        if line.find(key) >= 0:    #find()メソッドを使う
            print(i+1, ':', line)

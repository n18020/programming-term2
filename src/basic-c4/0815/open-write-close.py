#ファイルを開く
a_file = open('test.txt', mode='w', encoding='utf-8')

#ファイルに書き込む
a_file.write('私は失敗したことがない。\n')
a_file.write('ただ、一万通りの方法を\n見つけただけだ。\n')
a_file.write('ー　トーマス・エジソン\n')

#ファイルを閉じる
a_file.close()

#forと同じ働きをする関数を自作
def for_func(iterable, callback):
    it = iter(iterable)
    while True:
        try:
            v = next(it)
            callback(v)
        except StopIteration:
            break

#リストの内容をすべて画面に出力
nums = [1, 2, 3]
for_func(
    nums,   #リスト
    lambda i : print(i))   #繰り返す処理

#辞書方の内容をすべて画面に出力
ages = {'Taro':20, 'Jiro':15, 'Sabro':18}
for_func(
    ages.items(),   #（キー、値）のタプルを得る
    lambda n : print(n))    #繰り返す処理

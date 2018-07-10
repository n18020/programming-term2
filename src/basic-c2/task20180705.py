#支払金額
beer = 200 
otumami = 100
yakitori = 100

#個数
beer_c = 2
otumami_c = 1
yakitori_c = 2

#焼き鳥の割引率
rate = 0.2

#ポイントカードから引く料金
point = 150

#会計
payment = ((beer * beer_c) + (otumami * otumami_c) + (yakitori * (1 - rate) * yakitori_c)) - point

print(payment , '円')


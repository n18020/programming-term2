#花屋の支払い金額を求める
#値段
rose_v = 500
sun_v = 400
turip_v = 700
#個数
rose_c = 18
sun_c = 8-2
turip_c = 21-5
#割引率
rate = 0.1
#計算
sum_v = (rose_v * rose_c) + (sun_v * sun_c) + (turip_v * turip_c)
payment = sum_v * (1-rate)
#結果を表示
print('買い物の合計は',sum_v,'円')
print('割引してもらうと',payment,'円')

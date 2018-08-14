#二倍して一を引く方法
data = [ (i * 2 - 1) for i in range(1, 6)]
print(data)



#range()を工夫する方法
data = [ i for i in range(1, 11, 2)]
print(data)



#内容表記でforとifを組み合わせる方法
data = [ i for i in range(1, 11) if i % 2 == 1]
print(data)

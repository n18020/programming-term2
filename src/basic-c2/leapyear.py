year = int(input('西暦何年？'))

#うるう年かどうか判定
is_leap  = False
#４で割れたらうるう年
if year % 4 == 0:
    #１００で割れたらうるう年ではない
    if year % 100 == 0:
        #400で割れたらうるう年
        if year % 400 == 0:
            is_leap = True
        else:
            is_leap = False
    else:
        is_leap = True
else:
    is_leap = False

# 結果を表示
if is_leap:
    print('うるう年です')
else:
    print('平年です')

def _3_(parameter1, parameter2, calculation_method):

    print("四則計算プログラムです。")
true = True
# 第1パラメータに数字を入力
while True:
    parameter1 = input("第1パラメータを入力してください")
    para1 = str.isnumeric(parameter1)
    if para1 != true:
        print("入力が不正です。")
        continue
    break

# 第2パラメータに数字を入力
print("第1パラメータが確定しました。")
while True:
    parameter2 = input("第2パラメータを入力してください")
    para2 = str.isnumeric(parameter2)
    if para2 != true:
        print("入力が不正です。")
        continue
    print("第2パラメータが確定しました。")
    parameter1 = float(parameter1)
    parameter2 = float(parameter2)
    break

#演算方法を入力
while True:
    enzan = input("演算方法を入力してください\n")
    if enzan == "+":
        add = parameter1 + parameter2
        result = add
        break
    if enzan == "-":
        sub = parameter1 - parameter2
        result = sub
        break
    if enzan == "*":
        mul = parameter1 * parameter2
        result = mul
        break
    if enzan == "/":
        div = round((parameter1 / parameter2), 2)
        result = div
        break
    print("入力が不正です。")

print("結果は{}です。" .format(result))
help(_3_)

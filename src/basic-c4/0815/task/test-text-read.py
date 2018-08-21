records = {}
with open("test-record.txt", encoding="utf-8") as trt:
    for line in trt:
        lis = line.split(",")
        records[lis[0]] = int(lis[1])

sum_v = 0
for v in records.values():
    sum_v += v

ave_v = sum_v / len(records)
print("合計点:", sum_v)
print("平均点:", ave_v)

fmt = "| {0:<7} | {1:>4} | {2:>5}"
print("| 名前    | 点数 | 差")
for name, v in sorted(records.items()):
    # 平均点との差を求める
    diff_v = v - ave_v
    # 小数点以下を丸める
    diff_v = round(diff_v, 1)
    # 書式にそって出力
    print(fmt.format(name, v, diff_v))

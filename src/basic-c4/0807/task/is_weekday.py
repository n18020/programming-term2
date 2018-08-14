from datetime import datetime, timedelta

def process(target_date):
    """
    メインロジックを実行する
    Parameters
    ----------
    target_date : datetime
        処理対象の日付
    Returns
    -------
    list
        表示されるメッセージを要素に含むリスト
    """

    res_list = []   # 結果として返すリスト
    week = target_date.strftime("%a")
    ymd = target_date.strftime("%Y/%m/%d")

    if week == "Sat":
        res_list.append("{0} は {1} です。平日ではありません。".format(ymd, week))

        two_days_later = target_date + timedelta(days=2)
        res_list.append("次の平日は {0} です。".format(two_days_later.strftime("%Y/%m/%d")))

    elif week == "Sun":
        res_list.append("{0} は {1} です。平日ではありません。".format(ymd, week))

        tomorrow = target_date + timedelta(days=1)
        res_list.append("次の平日は {0} です。".format(tomorrow.strftime("%Y/%m/%d")))

    else:
        res_list.append("{0} は {1} です。平日です。".format(ymd, week))

    return res_list

def display(msgs):
    """
    結果を表示する
    Parameters
    ----------
    msgs: list
        表示するメッセージが格納されたリスト
    Returns
    -------
    なし
    """
    print(*msgs, sep="\n")

# メイン処理
if __name__ == '__main__':
    while True:
        try:
            input_date = input('日付を入力してください。')
            target_date = datetime.strptime(input_date, '%Y/%m/%d')

            display(process(target_date))
            break
        except:
            print('入力された日付が不正です。再入力してください。')

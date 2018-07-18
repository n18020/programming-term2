menu = {
    'Drip Coffee': 280,
    'ColdBrewCoffee': 320,
    'CafeLatte': 330,
    'SoyLatte': 380,
    'Cappuccino': 330,
    'CaramelFrappuccino': 470,
    'MacchaCreamFrappuccino': 470
}

option = {
    'LowFatMilk': 0,
    'NonFatMilk': 0,
    'SoyMilk': 50,
    'DeepCoffee': 60,
    'WhipCream': 70,
    'CaramelShrup': 60,
    'ChocoSource': 0,
    'DeCafe': 50
}
menu_v = []
menu_f = []

while True:
    choose_menu = input('メインメニューを入力してください:')
    if choose_menu in menu.keys():
        menu_v.append(choose_menu)
        menu_f.append(menu[choose_menu])
        break
    else:
        print('存在しないメニューです。')

print('メインメニューを承りました。')

while True:
    choose_option = input('オプションメニューを選んでください:')
    if choose_option in option.keys():
        menu_v.append(choose_option)
        menu_f.append(option[choose_option])
        break
    else:
        print('選択したオプションはありません')

pay = sum(menu_f)
print('注文内容は{}です'.format(menu_v))
print('合計金額は{}円です。右奥のカウンターにてお待ちください'.format(pay))


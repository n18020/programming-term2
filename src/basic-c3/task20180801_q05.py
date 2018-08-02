member_list = {
    'Aiba': 35,
    'Matsmoto': 34,
    'Ninomiya': 35,
    'Oono': 37,
    'Sakurai': 36}

age_list = sorted(
    member_list.items(),
    key=lambda x: x[1],
    reverse=True)

for name, age in age_list:
    print(name, age)

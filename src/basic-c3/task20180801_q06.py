member_list = {
    'Aiba': 175,
    'Matsmoto': 172,
    'Ninomiya': 168,
    'Oono': 166,
    'Sakurai': 171}

height_list = sorted(
    member_list.items(),
    key=lambda x: x[1])

for name, height in height_list:
    print(name, height)

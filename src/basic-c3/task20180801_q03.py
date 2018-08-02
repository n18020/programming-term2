TAX_RATE = 8

price = [13600, 14500, 16000, 11111, 11667]

includ_tax = lambda x: int(round(x * (1 + TAX_RATE / 100), -1))
print(list(map(includ_tax, price)))

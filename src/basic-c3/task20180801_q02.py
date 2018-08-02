TAX_RATE = 10

price = [13600, 14500, 16000, 11111, 11667]

includ_tax = lambda x: round(x * (1 + TAX_RATE / 100))
print(list(map(includ_tax, price)))

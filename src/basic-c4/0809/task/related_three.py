num = 0
aho = []

for num in range(1, 41):
    if num % 3 == 0 or num // 10 == 3 or num % 10 == 3:
        aho.append('アホ')
    else:
        aho.append(num)
print(aho)


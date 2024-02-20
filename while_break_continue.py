i = 2
while i%2 == 0:
    i = i*2
    if i == 64:
        continue
    elif i > 1024:
        break
    print(i)
    
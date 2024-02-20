friends = [
    ['Ayan', '24', 'TCS', 'Citi'],
    ['Nasir', '25', 'TCS', 'Royal London'],
    ['Kali', '24', 'TCS', 'Aegon'],
    ['Cartoon', '23', 'Bekar', 'Teacher']
]

print(friends)

for i in friends:
    print(i, end = " ")
    for j in i:
        print(j)
        for k in j:
            print(k)
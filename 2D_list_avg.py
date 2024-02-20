students_marks = [
    [100, 100, 100, 100, 100],
    [1, 1, 1, 1, 1]
]

for i in students_marks:
    t = 0
    sub = 0
    avg = 0
    sub = len(i)
    for j in i:
        t = t + j  
    avg = round((t/sub),2)
    if avg >= 90:
        print("A+")
    elif avg in range(80, 90):
        print("A")
    elif avg in range(70, 80):
        print("B")
    elif avg in range(60, 70):
        print("C")
    elif avg in range(50, 60):
        print("D")
    elif avg < 50:
        print("F")
q = ["2+2=?", "сколько дней требуется чтобы обойти экватор?", "что делал слон когда пришёл Наполеон?", "какая фигура занимает клетку Е1 в начале шахматной партии?", "столица исландии?"]
an = ["4", "364", "травку щипал", "белый король", "рейкьявик"]
an2 = ["четыре", "365", "траву жевал", "король", "Рейкьявик"]
count = 0
for i in range(len(q)):
    print(q[i])
    ans = str(input())
    if ans == an[i] or ans == an2[i]:
        count+=1
print("Верных ответов:", count)


map = {
    "Jakie masz na imie i nazwisko ?" : " ",
    "W jakich okolicznościach czytasz książki najczęściej ? " : ["podczas podróży", " w ogóle nie czytam"," w czasie wolnym"],
"Po jakie gatunki książek sięgasz najczęściej ? " : [ " horrory","naukowe","fantastyke"],
    "W jakim języku książki czytasz ? " : ["polskim","angielskim","rosyjskim"]
}


answers = []

for x in map.keys():
    c = 1
    if type(map[x]) is list:
        print(x)
        for a in map.get(x):
            print(c, ". ", a)
            c= c+1
        ans_num = input("Podaj numer odpowiedzi: ")
        answers.append(int(ans_num)-1)
    else:
        ans = input(x)
        answers.append(ans)

print(answers)
c = 0
for x in map.keys():

    print("pytanie: ", x)
    if type(map[x]) is list:
        print("odpowiedz: ", map.get(x)[int(answers[c])])
    else:
        print("odpowiedz: ", answers[c])
    c = c + 1







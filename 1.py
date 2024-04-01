with open("astronaut_time.csv", encoding="UTF-8") as f:
    spisok = []
    c = []
    g = []
    d, h = [], []
    for s in f:
        a = [elem for elem in s.strip('\n').split(',')]
        spisok += [a]
    for elem in spisok[1:]:
        c.append(elem[3].split(':'))
        g.append(elem[4])
for i in c:
    d.append(i)
for j in g:
    h.append(j)
for i in range(len(d)):
    newtime = int(d[i][0]) + int(h[i])
    d[i][0] = str(newtime)
    if d[i][0] == '24':
        d[i][0] = '00'
    if len(d[i]) == 1:
        d[i] = '0' + d[i]


with open('astronaut_time.csv', encoding='UTF-8', mode='w') as new_time:
    new_time.write(d[0][0] + ':' + d[0][1] + ':' + d[0][2])
    new_time.write('0' + d[1][0] + ':' + d[1][1] + ':' + d[1][2])
    new_time.write(d[2][0] + ':' + d[2][1] + ':' + d[2][2])



print(d[0][0] + ':' + d[0][1] + ':' + d[0][2])
print('0' + d[1][0] + ':' + d[1][1] + ':' + d[1][2])
print(d[2][0] + ':' + d[2][1] + ':' + d[2][2])
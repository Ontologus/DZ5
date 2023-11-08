n = int(input())
nlist = {}
for i in range(n):
    city = input()
    if city in nlist:
        nlist[city] += 1
    else:
        nlist[city] = 1
rcount = 0
for city, count in nlist.items():
    if count > 1:
        rcount += 1
print(rcount)
#Здесь вычисляется количество городов, которые повторяются, как в задании

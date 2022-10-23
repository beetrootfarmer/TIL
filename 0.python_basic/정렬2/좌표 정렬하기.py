# def coor(n):
#     for i in range(len(n)):
#         for j in range(len(n) - 1):
#             if  (n[j][0] + n[j][1]) > (n[j + 1][0] + n[j + 1][1]):
#                 n[j + 1], n[j] = n[j], n[j + 1]

def coor(a):
    if len(a) <= 1:
        return a
    center = len(a) // 2

    l = coor(a[:center])
    r = coor(a[center:])

    i , j = 0, 0
    buff = [0 for _ in range(len(a))]

    while i < len(l) and j < len(r):
        if (l[i][0] + l[i][1]) < (r[j][0] + r[j][1]):
            buff.append(l[i])
            i += 1
        else :
            buff.append(r[j])
            j += 1

    buff += l[i:]
    buff += r[j:]
    
    return buff

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
coor(a) #coordinate
for x, y in a:
   print(x, y)
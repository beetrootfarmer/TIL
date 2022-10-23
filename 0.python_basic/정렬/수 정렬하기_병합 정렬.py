

def merge_sort(a):
    def m_sort(a, l, r):
        if l < r:
            center = (l + r) // 2
            m_sort(a, l , center)
            m_sort(a, center + 1, r)

            p = j = 0
            i = k = l

            while i <= center:
                buff[p] = a[i]
                p += 1
                i += 1
            
            while i <= r and j < p:
                if buff[j] <= a[i]:
                    a[k] = buff[j]
                    j += 1
                else:
                    a[k] = a[i]
                    i += 1
                k += 1

            while j < p:
                a[k] = buff[j]
                k += 1
                j += 1
    n = len(a)
    buff = [None] * n
    m_sort(a, 0, n - 1)
    del buff

num = int(input())
a = []
for _ in range(0, num):
    a.append(int(input()))
merge_sort(a)
for i in range(num):
    print(a[i])

# 시간초과
#  pypy로 해야 시간초과가 나지 않는다고 한다 

def merge_sort(a):
    if len(a) <= 1:
        return a
    center = len(a) // 2

    l = merge_sort(a[:center])
    r = merge_sort(a[center:])

    i , j, k = 0, 0, 0
    buff = []

    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            buff.append(l[i])
            i += 1
        else :
            buff.append(r[j])
            j += 1

    buff += l[i:]
    buff += r[j:]
    
    return buff

N = int(input())
a = []
for _ in range(N):
    a.append(int(input()))

a = merge_sort(a)

for i in a:
    print(i)


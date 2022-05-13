#======================버블정렬==========================
# def bubble(a):
#     n = len(a)
#     for i in range(n - 1):
#         for j in range(n - 1, i - 1):
#             if a[j - 1] > a[j]:
#                 a[j - 1], a[j] = a[j], a[j - 1]

# N = int(input())
# a = []
# for _ in range(0, N):
#     a.append(int(input()))
# bubble(a)
# for i in range(N):
#     print(a[i])

#======================선택정렬==========================
def select(a):
    n = len(a)
    for i in range(n - 1):
        min = i
        for j in range(i + 1, n):
            if a[j] < a[min]:
                min = j
        a[i], a[min] = a[min], a[i]

N = int(input())
a = []
for _ in range(0, N):
    a.append(int(input()))
select(a)
for i in range(0, N):
    print(a[i])
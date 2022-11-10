#  3의 거듭제곱 수인 N 이 주어졌을 떄 
# N * N 만큼의 사각형을 그리는데
#  재귀 활용해서 패턴을 찍어야함.

#  N이 3보다 크면 가운데 공백을 만들어야함 

# def tree_star(N, count):
#     if (N % 3) != 0:
#         return()
#     if (count != N):
#         m = N // 3
#         for i in range(0, N):
#             if (i == (N - 1)):
#                 print ("*")
#             elif ((count - 1) % 3 == 0) and ((i - 1) % 3 == 0):
#                 print (" ", end='')
#             elif (m <= count < m * 2) and (m <= i < m * 2):
#                 print (" ", end='')
#             else :
#                 print("*", end='')
#         tree_star(N, count + 1)
# N = int(input())
# count = 0
# tree_star(N, count)

#  왜 런타임에러..
# import sys
# sys.setrecursionlimit(10 ** 6)
# def tree_star(N, count):
#     if (N % 3) != 0:
#         return()
#     if (count != N):
#         m = N // 3
#         for i in range(0, N):
#             if (i == (N - 1)):
#                 print ("*")
#             elif ((count - 1) % 3 == 0) and ((i - 1) % 3 == 0):
#                 print (" ", end='')
#             elif (m <= count < m * 2) and (m <= i < m * 2):
#                 print (" ", end='')
#             else :
#                 print("*", end='')
#         tree_star(N, count + 1)
# N = int(input())
# count = 0
# tree_star(N, count)

# 왜 틀려..


# N = int(input())
# m = N // 3
# for count in range (0, N):
#     if (count != N):
#         for i in range(0, N):
#             if (i == (N - 1)):
#                 print ("*")
#             elif ((count - 1) % 3 == 0) and ((i - 1) % 3 == 0):
#                 print (" ", end='')
#             elif (m <= count < m * 2) and (m <= i < m * 2):
#                 print (" ", end='')
#             else :
#                 print("*", end='')

# 왜 틀려..
#  잘못된 부분이 있다는걸 방금 알았네 하하하하하핳 다시해

def tree_star(N, count, m1):
    if (N % 3) != 0:
        return()
    for j in range(0,len(m1)):
        if (m1[j] <= count < m1[j] * 2):
            m = m1[j]
    
    if (count != N):
            #m = (N // 3) # 9일 때 3/ 27일때 3,9 / 81일때 3, 9, 27 / 243 일때 3, 9, 27, 81 ... 
        for i in range(0, N // 9):
            if (i == (N - 1)):
                print ("*")
            elif ((count - 1) % 3 == 0) and ((i - 1) % 3 == 0):
                print (" ", end='')
            elif (m <= count < (m * 2)) and (m <= i < (m * 2)):
                print (" ", end='')
            else :
                print("*", end='')
        tree_star(N, count + 1, m1)
N = int(input())
count = 0
num = N
m = []
i = 0
while ((num//3) >= 3):
    num = num // 3
    m.append(num)
tree_star(N, count, m)
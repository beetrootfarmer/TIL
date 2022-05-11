# N = int(input())
# sum = 1
# if (N == 0):
#     print (sum)
# else :
#     while (1):
#         sum *= N
#         N -= 1
#         if (N == 1):
#             break
#     print (sum)
# 시간초과?!!!!!!!!!!

# N = int(input())
# sum = 1
# if (N < 0):
#     print (0)
# elif (N == 0):
#     print (sum)
# else :
#     while (N > 1):
#         sum *= N
#         N -= 1
#     print (sum)

# 생각해보니까 단원이 재귀네..
# 재귀로 다시 풀어봄

def facto(N):
    if (N < 0):
        return (0)
    elif (N == 0):
        return (1)
    else :
        return(N*facto(N-1))
N = int(input())
print(facto(N))
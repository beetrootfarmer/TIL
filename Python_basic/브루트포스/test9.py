l1 = [1,2,3]
l2 = l1[:]
l3 = l2
l1.append('a')
l2.append('b')
l3.append('c')

print(l1)
print(l2)
print(l3)


# from unittest import result

# print(5*False)

# num = 100
# result = str(num)

# if num >= 1000:
#     result = str(num // 1000) + 'k'
# elif num >= 0:
#     pass
# print(result)

#print(2 or 3)

# def fibo (n):
#     if n < 2:
#         return n
#     else:
#         return fibo(n-1) + fibo(n-2)
# print(fibo(5))

# def ko_num(num):
#     d = {0:'영', 1:'일',2:'이', 3:'삼',4:'사', 5:'오',6:'육', 7:'칠', 8:'팔', 9:'구'}
#     return d[num]
# print(ko_num(3) + ko_num(6))

# num = 5
# for i in range(1, num + 1):
#     print(i, i*i)

# a = 80
# b = 30
# a = a - b
# print(a)

# x = 1

# def outer():
#     x = 8
#     def inner():
#         x = 3
#     inner()
#     print(x)
# x = 4

# outer()
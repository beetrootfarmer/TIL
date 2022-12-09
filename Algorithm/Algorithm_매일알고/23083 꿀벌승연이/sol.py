# N, M = map(int,input().split())
# K = int(input())
# blanks = [tuple(map(int,input().split())) for _ in range(K)]

# print(blanks)


print('------')
def matrix_mult(A, B, n):
    temp = [[0]*2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                temp[i][j] += (A[i][k] * B[k][j])
    print('temp===', temp, 'n: ', n, 'A:',A, ' B:', B)
    return temp

def matrix_pow(n, M):
    if n == 1: return M
    if n%2 == 0:
        temp = matrix_pow(n//2, M)
        return matrix_mult(temp, temp, n)
    else:
        temp = matrix_pow(n-1, M)
        return matrix_mult(temp, M, n)
A = [[1, 1], [1, 0]]
print(matrix_pow(8-1, A)[0][0])
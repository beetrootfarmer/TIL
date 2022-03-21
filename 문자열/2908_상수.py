# 주어진 두 수 중 큰 수를 찾기

#문자열 뒤에서부터 출력 
# [::1] 앞에서 부터 하나씩
#[::2] 앞에서부터 두개씩 0,2,4,6
#[::-1] 뒤에서부터 하나씩
#[::-2] 뒤에서부터 두개씩 -1, -3, -5, -7
m,n = input().split()
m = m[::-1]
n = n[::-1]
print(max(int(m),int(n)))

# 다른 사람의 답
a, b =input().split()

def reading(k):
    k = k[::-1]
    return int(k)

print(max([reading(a),reading(b)]))

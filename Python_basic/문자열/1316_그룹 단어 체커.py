# 그룹단어 : 연속해서 나타나는 문자 
# happy는 그룹단어
# happyh 는 h가 떨어져 있기 때문에 그룹단어가 아님 

# 테스트 케이스 개수
# 그룹단어 변수 선언
# 그룹단어 출력 반복문
# 그룹단어 개수 출력
N = int(input())
g = 0
for i in range(N):
    st = input()
    # 연속된 문자열 중복제거
    for j in range(0,len(st)-1):
        if st[j] == st[j+1] :
           st = st.replace(st[j],' ')
    st = st.replace(' ','')
    s = ''.join(dict.fromkeys(st))

    if s == st :
        g += 1
    else : 
        g += 0
    # 문자열에 중복된 문자가 있는지 확인 
print(g)


N = int(input())
g = 0
for i in range(N):
    st = list(input())
    ind = 0
    while ind < len(st)-1:
        if st[ind] == st[ind+1] :
           st.pop(ind+1)
        else:
            ind += 1
    if len(st) == len(set(st)) :
        g += 1
print(g)
   
#다른사람 답
N = int(input())
result = N
for i in range(0,N):
    word=input()
    for j in range(0,len(word)-1):
        if word[j]==word[j+1]:
            pass
        elif word[j] in word[j+1:]: #중복 제거 이후 뒤에도 같은 문자열이 있다면 그룹단어가 아님!
            result-=1
            break
print(result)

#다른사람 답 2
result = 0
for i in range(int(input())):
    word = input()
    if list(word) == sorted(word, key=word.find):
        result += 1
print(result)
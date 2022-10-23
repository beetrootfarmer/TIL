T = int(input())
for tc in range(1, T+1):
    N = int(input())

    num = N ** (1/3)     # 세제곱근 구하기
    fd = str(num).find('.')                                     # 소수점(.)의 인덱스 번호 찾기
    if str(num)[-1] == '0' and str(num)[-2] == '.' :            # 소수점 뒤에 0이 있으면 int로 형변환
        num = (int(num))
    elif str(num)[fd+1] == '9' and str(num)[fd+2] == '9':      # 소수점 첫째자리가 둘째자리가 둘다 9이면 int로 형변환 후 +1
        num = (int(num)+1)
    else:                                                       # 나머지는 -1
        num = -1

    print(f'#{tc} {num}')
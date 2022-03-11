# 입력 문자를 소문자 출력 lower() / 최대길이 50자 설정
id = input().lower()

if ( len(id) < 51) : 
    print(id + "??!")
else :
    print("글자수 길이가 50자를 초과했습니다")
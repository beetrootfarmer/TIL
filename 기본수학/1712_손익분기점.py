# 월드전자의 
# 고정비용 A
# 노트북 한 대 값 = n(이익)  + 가변비용 B = C 
# 손익분기점은 투자비용 < 판매수입 
# 즉 A + B*N(고정비용 + 가변비용*판매량) < C*N(판매가격*판매량) 일때 N
# 최초로 이익이 발생하는 판매량 N은? 

a, b , c= map(int, input().split())
if b >= c :
    print(-1)
else :
    print(int(a/(c - b) + 1))

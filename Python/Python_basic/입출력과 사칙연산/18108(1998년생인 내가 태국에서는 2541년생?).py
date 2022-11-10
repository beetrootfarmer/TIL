year = input()
if (1000<= int(year) <= 3000) :
    print(int(year)-543)
elif (year.isdigit( ) == False): 
    print("숫자를 입력하세요") 
else : print("1000에서 3000사이의 숫자를 입력하세요")
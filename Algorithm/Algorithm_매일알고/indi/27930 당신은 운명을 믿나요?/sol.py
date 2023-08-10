import sys
input = sys.stdin.readline

str = str(input())

K = "KOREA"
Y = "YONSEI"
result = ""

if "K" not in str:
    print("YONSEI")
elif "Y" not in str:
    print("KOREA")
else:
    for i in str:
        if not K:
           result = "KOREA"
           break
        elif not Y:
            result = "YONSEI"
            break
        if i == K[0]:
            K = K.replace(i, "")
            continue
        if i == Y[0]:
            Y = Y.replace(i, "")
            continue
    print(result)

case = int(input())
for i in range(case):
    fl = int(input())
    ho = int(input())
    count=0
    for i in range(fl):
        for i in range(1,ho+1):
            count += i
    print(count)

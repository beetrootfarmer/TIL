# 배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 구하려 합니다.

# 예를 들어 array가 [1, 5, 2, 6, 3, 7, 4], i = 2, j = 5, k = 3이라면

# array의 2번째부터 5번째까지 자르면 [5, 2, 6, 3]입니다.
# 1에서 나온 배열을 정렬하면 [2, 3, 5, 6]입니다.
# 2에서 나온 배열의 3번째 숫자는 5입니다.
# 배열 array, [i, j, k]를 원소로 가진 2차원 배열 commands가 매개변수로 주어질 때, commands의 모든 원소에 대해 앞서 설명한 연산을 적용했을 때 나온 결과를 배열에 담아 return 하도록 solution 함수를 작성해주세요.

# array의 길이는 1 이상 100 이하입니다.
# array의 각 원소는 1 이상 100 이하입니다.
# commands의 길이는 1 이상 50 이하입니다.
# commands의 각 원소는 길이가 3입니다.


# 중요한것! 
# 배열 슬라이싱 ~~~~~~~~~ a[start : end : step] a[start:end]
# def solution(array, commands):
#     answer = []
#     for n in range(len(commands)): #주어진 테스트케이스만큼 반복 
#         i = commands[n][0] -1
#         j = commands[n][1] -1
#         k = commands[n][2] -1
#         new = []
#         new = array[(i):(j)]
#         new.sort() #리스트 숫자 순서대로 정렬 
#         answer.append(new[k])
#     return answer

def solution(array, commands):
    answer = []
    for n in range(0,len(commands)):
        i = commands[n][0] -1
        j = commands[n][1] 
        k = commands[n][2] -1
        new = []
        if i==j: 
            #new = array[i] # 이렇게하면 리스트가 아니라 int가 들어간다 
            answer.append(array[i])
        else : 
            new = array[(i):(j)]
            new.sort() 
            answer.append(new[k])
    return answer

# array = list(input())
# commands = []
# for i in range(3): #2차원배열 세로길이가 3일 때 for문으로 입력받기 
#     commands.append(list(map(int,input().split())))
array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2,5,3],[4,4,1],[1,7,3]]
print(solution(array,commands))


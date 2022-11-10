# 위 그림의 경로를 표현하는 문자열은 EEESEEEEEENNNN입니다. 빨간색 화살표로 표시한 지점에서 내비게이션은 안내 메시지를 보내게 됩니다.
# 출발 직후 300m 앞에서 오른쪽으로 방향을 바꾸어야 하므로 내비게이션은 다음과 같이 안내 메시지를 보냅니다.
# Time 0: Go straight 300m and turn right

# 처음 방향 변경 직후, 100m 앞에서 왼쪽으로 방향을 바꾸어야 하므로 내비게이션은 다음과 같이 안내 메시지를 보냅니다.
# Time 3: Go straight 100m and turn left

# 이번 방향 변경 뒤에, 100m만큼 직진 후 500m 앞에서 왼쪽으로 방향을 바꾸어야 하므로 내비게이션은 다음과 같이 안내 메시지를 보냅니다.
# Time 5: Go straight 500m and turn left

# 남은 경로는 방향 변경 없이 직진하면 배달지에 도착하므로 내비게이션의 안내는 종료됩니다.
# 경로를 담은 문자열 path가 매개변수로 주어졌을 때, 내비게이션의 안내 메시지를 시간 순서대로 배열에 담아서 return 하도록 solution 함수를 완성해주세요.
# 단, 내비게이션의 안내 메시지가 적어도 하나 이상 있는 경우만 주어집니다.

# "EEESEEEEEENNNN"

# ["Time 0: Go straight 300m and turn right",
# "Time 3: Go straight 100m and turn left",
# "Time 5: Go straight 500m and turn left"]
p = str(input())

def solution(path):
    patharr= []
    for i in path:
        patharr.append(i)
    answer =[]
    count = 1
    time = 0
    nowon = str(patharr[0])
    d = ""

    def direction(dir):
        if dir == 'E':
            direct = 1
        elif dir == 'S':
            direct = 2
        elif dir == 'W':
            direct = 3
        else: direct = 4
        return int(direct)
    
    
    for i in range(1,len(path)):
        if i == int(len(path)-1): #마지막이면 더이상 추적X break
            break
        else : 
            if nowon == str(patharr[i]) :
                count += 1
            else:
                if (direction(nowon)-direction(patharr[i]) == 1 ) or (direction(nowon)-direction(patharr[i]) == -3) :
                    d = 'left'
                else : d = 'right'
                if count > 5:
                    n = count - 5
                    count = 5
                    time += n
                    # if time == 0 :
                    #     time = 1
                answer.append("Time "+ str(time)+": "+"Go straight "+str(count*100)+"m and turn "+d)
                time += count
                count = 1
            nowon = str(patharr[i])
    return answer

print(solution(p))

# 실행한 결괏값 ["Time 0: Go straight 300m and turn right","Time 3: Go straight 100m and turn left","Time 5: Go straight 500m and turn right"]이(가) 
# 기댓값 ["Time 0: Go straight 300m and turn right","Time 3: Go straight 100m and turn left","Time 5: Go straight 500m and turn left"]와(과) 다릅니다.
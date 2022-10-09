import sys
sys.stdin = open('input.txt')

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

# p와 q를 분리해서 계산할것임
mw = t%(2*w)
mh = t%(2*h)

if mw + p <= w: p = mw + p                  # p의 위치에서 w방향으로 mw만큼 나간 것 
elif mw + p <= 2 * w: p = w-(mw + p - w)    # w - (p의 위치에서 w를 찍고 돌아온거리)
else: p = mw + p - 2*w                      # mw + p가 2*w보다 큰 경우 (2*w < x <= (2*w -1)+w)
                                        
if mh + q <= h: q = mh + q
elif mh + q <= h * 2: q = h - (mh + q - h)
else: q = mh + q - 2 * h
print(p, q)

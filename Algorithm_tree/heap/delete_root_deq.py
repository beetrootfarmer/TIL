def deq():
    global last
    tmp = heap[1]
    heap[1] = heap[last]
    last -= 1
    p = 1
    c = p * 2
    while c <= last: # 자식이 하나라도 있으면 
        if c + 1 <= last and heap[c] < heap[c+1]: #오른쪽 자식이 있고 오른쪽이 더 크면
            c += 1
        if heap[p] < heap[c] :  # 부모가 더 작으면 자식이랑 교환하는 것 반복 
            heap[c], heap[p] = heap[p], heap[c]
            p = c
            c = p*2
        else:
            break    
    return tmp

def enq(n):
    global last
    last += 1
    heap[last] = n
    c = last
    p = c//2
    while p and heap[p] < heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c//2
heap = [0] * 100
last = 0
enq(2)
enq(5)
enq(7)
enq(3)
enq(4)
enq(6)
while last:
    print(deq())
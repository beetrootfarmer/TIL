def solution (s, k):
    answer = ''
    len_s = len(s)
    lst = list(s)
    counter = 0

    for i in range(len_s):
        if counter == k:
            break
        max_char = lst[i]
        max_char_idx = i
        for c in range(i+1, len_s):
            if lst[c] > lst[i] and lst[c] > max_char:
                max_char = lst[c]
                max_char_idx = c
        if max_char == lst[i]:                # 본인보다 큰 글자가 없는 경우
            continue
        else:
            lst[i] , lst[max_char_idx] = max_char, lst[i]   # 가장 큰 글자와 교환
        counter += 1
    print(''.join(lst))
    return answer

solution('eedcab', 3)
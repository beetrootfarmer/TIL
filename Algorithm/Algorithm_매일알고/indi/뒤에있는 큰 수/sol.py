def solution(numbers):
    ln = len(numbers)
    answer = [-1] * ln
    stack = []
    for i, val in enumerate(numbers):
        while stack and numbers[stack[-1]] < val:
            answer[stack.pop()] = val
        stack.append(i)
    return answer;
solution([2,3,3,5])

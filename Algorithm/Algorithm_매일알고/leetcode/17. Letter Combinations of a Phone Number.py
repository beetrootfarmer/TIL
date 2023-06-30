# 천지인 자판에서 숫자 조합이 만들어낼 수 있는 모든 경우의 문자열을 리스트에 담아서 리턴해라
# 딕셔너리를 만들어서 첫번째 숫자의 문자열을 순회하면서 조합을 만들고 stack에 담아줍니다
# 재귀 시간복잡도 O(N)

code = {'1':[], '2':['a','b','c'], '3':['d', 'e' ,'f'], '4':['g','h', 'i'], '5':[ 'j','k','l'], '6':['m','n','o'], '7':['p','q','r','s'], '8':['t','u','v'], '9':['w','x','y','z'], '0':[' ']}
def letterCombinations(digits):
    stack = []
    lenDigits = len(digits)

    def DFS(num, word, l, digits):
        if num == l:
            if word not in stack:
                stack.append(word)
            return
        for char in code[digits[num]]:
            num += 1
            DFS(num, word+char, l, digits)
            num -= 1
    if lenDigits:
        DFS(0, '', lenDigits, digits)
    return stack

a = letterCombinations("23")
print(a)
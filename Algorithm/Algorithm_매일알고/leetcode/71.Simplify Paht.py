# Unix 스타일의 파일경로를
# canonical 경로로 단순화시키세요
#
# Unix format
#   .: 현재디렉토리
#   ..: 상위디렉토리
#   //: /
#   …: 파일 혹은 폴더명
#
# canonicalformat
#   single slash로 시작
#   두개의 디렉토리는 single slash로 분리
#   끝에 붙은 / 는 없음(no trailing /)
#   상위경로로 이동하는 옵션이 없음( /../ -> / )

# 한번의 순회 -> O(N)
def simplifyPath(path):
    result = '/'

    # 중간 슬레시는 //로 들어간다
    # / 기준으로 split 한 리스트를 순회하며 stack에 담아준다
    stack = []
    words = path.split('/')
    for w in words:
        if not w or w == '.':
            continue
        if w == '..':
            if stack:
                stack.pop()
        else:
            stack.append(w)
    return result + '/'.join(stack)

a = simplifyPath("/../")
print(a)
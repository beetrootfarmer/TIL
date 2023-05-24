import itertools
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

combi = list(map(list,itertools.combinations(range(1,N+1), M)))
for c in combi:
    print(' '.join(list(map(str,c))))
print('---------------절취선 [31256kb 40ms]---------------------')
ans = []
def backtrack():
    if len(ans) == M:
        print(" ".join(list(map(str,ans))))
        return
    for i in range(1, N+1):
        if i not in ans:
            if len(ans) == 0 or (len(ans) > 0 and i > ans[-1]): # 내림차순 배열은 만들지 않도록 했음
                ans.append(i)
                backtrack()
                ans.pop()
backtrack()
print('---------------절취선 [2020kb 0ms]---------------------')
# include <iostream>
# include <vector>
# include <algorithm>
# using namespace std;
#
# vector < int > s;
# int
# e[9] = {};
# void dfs(int n, int N, int M){
#     if (s.size() == M){
#         for (auto i: s)cout << i << " ";
#         cout << "\n";
#         return;
#         }
#
#     for (int i=n; i <= N; i++){
#         s.push_back(i);
#         dfs(i + 1, N, M);
#         s.pop_back();
#         }
#     }
# int main() {
#     int N, M;
#     cin >> N >> M;
#     dfs(1, N, M);
#     }
# 백트래킹

재귀적으로 문제를 해결하되 현재 재귀를 통해 확인 중인 상태가 제한 조건에 위배 되는지 판단하고, 해당 상태가 이ㅜ배되는 경우 해당 상태를 제외하고 다음 단계로 넘어간다.

해를 찾는 도중 해가 절대 될 수 없다고 판단되면, 되돌아가서 다시 해를 찾는다.

### 가지치기

더 이상 탐색할 필요가 없는 상태를 제외한다.

백트래킹은 모든 경우의 수에서 조건을 만족하는 경우를 탐색하는 것이기 때문에 완전탐색기법인 dfs, bfs로 모두 구현이 가능하다.

특성상 조건에 부합하지 않으면 이전 수행으로돌아가야 함으로, dfs가 더 구현하기 편하다.

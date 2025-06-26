def solution(info, n, m): #재귀 함수 + 메모이제이션 사용
    from functools import lru_cache # 메모이제이션
    N = len(info)
    
    @lru_cache(maxsize=None)
    def dfs(i, a_sum, b_sum): #깊이 우선 탐색 함수 dfs
        if a_sum >= n or b_sum >= m:
            return float('inf') #무한대
        
        if i == N:
            return a_sum
        
        a_choice = dfs(i + 1, a_sum +info[i][0], b_sum)
        
        b_choice = dfs(i+1,a_sum, b_sum + info[i][1])
        return min(a_choice, b_choice)
    
    result = dfs(0,0,0)
    
    return result if result != float('inf') else -1
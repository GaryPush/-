class Solution1:
    ''' O(KN^2) '''
    def superEggDrop(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        
        >>> superEggDrop(1, 5)
        5
        >>> superEggDrop(5, 1)
        1
        """
        self.cache = [[None for _ in range(N+1)] for _ in range(K+1)]
        return self.mem(K, N)
        
    def minimax(self, K, N):
        if K == 1:
            return N
        if N <= 1:
            return 1
        res = N
        for i in range(1, N+1):
            res = min(res, 1 + max(self.mem(K-1, i-1), self.mem(K, N-i)))
        return res
    
    def mem(self, K, N):
        if self.cache[K][N] == None:
            self.cache[K][N] = self.minimax(K, N)
        return self.cache[K][N]


class Solution2:
    ''' 
    O(KlogN) 
    When I have m-1 moves and k-1 eggs, I can check dp[m-1][k-1] floors.
    But when I get 1 more move and 1 more egg, I start at floor dp[m-1][k-1]+1, because I know
    floors below that can be checked within m-1 moves and k-1 eggs.
    The best outcome is that the egg is not broken, we can then start from there and check dp[m-1][k]
    more floors.
    So the maximum floors I can check with m moves and k eggs is dp[m-1][k-1]+dp[m-1][k]+1
    '''
    def superEggDrop(self, K, N):
        '''
        dp[m][k] means the maximum number of floor that we can check with K eggs and M moves.
        '''
        dp = [[0] * (K + 1) for i in range(N + 1)]
        for m in range(1, N + 1):
            for k in range(1, K + 1):
                dp[m][k] = dp[m - 1][k - 1] + dp[m - 1][k] + 1
            if dp[m][K] >= N: return m

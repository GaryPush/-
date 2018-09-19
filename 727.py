class Solution(object):
    ''' https://leetcode.com/problems/minimum-window-subsequence/description/'''
    def minWindow(self, S, T):
        """
        dp[i][j] means the smallest end index of the substring in S[i:] and T[j:]
        :type S: str
        :type T: str
        :rtype: str
        """
        m,n = len(S),len(T)
        dp = [[None for _ in range(n)] for _ in range(m+1)]
        for j in range(n):
            dp[m][j] = -1  # S is empty, impossible to find the index
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if S[i] == T[j]:
                    if j == n-1:  # only one character in T
                        dp[i][j] = i  # i is the end index
                    else:
                        dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = dp[i+1][j]
        # find the minimum substring
        left = None
        right = None
        for i in range(m):
            if left == None or (dp[i][0] != -1 and dp[i][0]-i < right-left):
                left = i
                right = dp[i][0]
        if left != None:
            return S[left:right+1]
        return ''
        
        

class Solution:
    '''
    Backtracking
    O(2^N)
    
    '''
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = set()
        self.minRemoved = len(s)
        self.backtrack(s, 0, '', res, 0, 0)
        return list(res)
    
    def backtrack(self, s, currIndex, currStr, res, count, removed):
        if currIndex == len(s):
            if count == 0 and removed <= self.minRemoved:
                res.add(currStr)
                self.minRemoved = removed
            return
        if s[currIndex] == '(':
            self.backtrack(s, currIndex+1, currStr+'(', res, count+1, removed)
            if removed < self.minRemoved:
                self.backtrack(s, currIndex+1, currStr, res, count, removed+1)
        elif s[currIndex] == ')':
            if count > 0:
                self.backtrack(s, currIndex+1, currStr+')', res, count-1, removed)
            if removed < self.minRemoved:
                self.backtrack(s, currIndex+1, currStr, res, count, removed+1)
        else:
            self.backtrack(s, currIndex+1, currStr+s[currIndex], res, count, removed)

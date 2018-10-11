class Solution1(object):
    '''
    O(mn^2)
    '''
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        self.cache = [[None for _ in range(m+1)] for _ in range(len(nums)+1)]
        return self.memo(nums, 0, m)
        
    def helper(self, nums, start, m):
        if m == 1:
            return sum(nums[start:])
        if m == len(nums)-start:
            return max(nums[start:])
        res = sys.maxsize
        left = 0
        for i in range(start, len(nums)-m+1):
            left += nums[i]
            right = self.memo(nums, i+1, m-1)
            res = min(res, max(left, right)) # minimax
            if left > right:
                break
        return res
            
    def memo(self, nums, start, m):
        if self.cache[start][m] == None:
            self.cache[start][m] = self.helper(nums, start, m)
        return self.cache[start][m]

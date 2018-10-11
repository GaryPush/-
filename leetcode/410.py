class Solution1(object):
    '''
    Memoization
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

class Solution2(object):
    '''
    Binary search
    O(Nlog(sum of nums))
    '''
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        left = max(nums) # max split (m == len(nums))
        right = sum(nums) # min split (m == 1)
        while left < right:
            mid = (left+right) // 2
            numOfSubs = self.getNumOfSubs(nums, mid) # target max sum is mid, calculate minimum number of subarrays needed
            if numOfSubs > m:
                left = mid + 1
            else:
                right = mid
        return left
    
    def getNumOfSubs(self, nums, targetSum):
        currSum = 0
        res = 1
        i = 0
        while i < len(nums):
            if currSum+nums[i] <= targetSum:
                currSum += nums[i]
                i += 1
            else:
                res += 1
                currSum = 0
        return res

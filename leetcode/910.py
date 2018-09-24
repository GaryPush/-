class Solution(object):
    ''' 
    time: O(NlogN)
    space: O(1)
    
    If we add K to every A[i], then the range is A[-1]-A[0].
    - Why do we only campare every A[i]+K and A[i+1]-K?
    1. We don't have to worry about A[i]-K and A[i+1]+K because it is worse than A[i]+K and A[i+1]+K.
    2. If we compare A[i]+K and A[i+2]-K, either A[i+1]+K >= A[i] or A[i+1]-K <= A[i+2]-K. So it is always
    right to assume result list looks like [A[0]+K,A[1]+K,...,A[i]+k,A[i+1]-K,...,A[-1]-K].
    '''
    def smallestRangeII(self, A, K):
        A.sort()
        mi, ma = A[0], A[-1]
        ans = ma - mi
        for i in xrange(len(A) - 1):
            a, b = A[i], A[i+1]
            ans = min(ans, max(ma-K, a+K) - min(mi+K, b-K))
        return ans

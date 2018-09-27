class Solution1(object):
    '''
    time: O(knlog(kn))
    space: O(kn)
    
    Dijkstra
    '''
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs:
            return 0
        pq = []
        for i in range(len(costs[0])):
            pq.append([costs[0][i],0,i])
        heapify(pq)
        visited = [[False for _ in costs[0]] for _ in costs]
        while pq:
            cost,row,col = heappop(pq)
            if row == len(costs)-1:
                return cost
            if visited[row][col]:
                continue
            visited[row][col] = True
            for i in range(len(costs[0])):
                if i != col:
                    heappush(pq, [cost+costs[row+1][i],row+1,i])

class Solution2(object):
    '''
    time: O(kn)
    space: O(1)
    '''
    def minCostII(self, costs):
        """
        costs[i][j] means the minimum cost from house 0 to i, which is the sum of costs[i][j] and prev smallest 
        (or second prev smallest if color is the same)
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs:
            return 0
        min1,min2 = -1,-1 # keep track of prev smallest and second smallest
        for i in range(len(costs)):
            last1,last2 = min1,min2
            min1,min2 = -1,-1
            for j in range(len(costs[0])):
                if j != last1 and last1 != -1: # different color to smallest
                    costs[i][j] += costs[i-1][last1]
                elif j == last1 and last2 != -1: # same color to smallest, take second smallest then
                    costs[i][j] += costs[i-1][last2]
                if min1 == -1 or costs[i][j] <= costs[i][min1]:
                    min2 = min1
                    min1 = j
                elif min2 == -1 or costs[i][j] < costs[i][min2]:
                    min2 = j
        return costs[-1][min1]

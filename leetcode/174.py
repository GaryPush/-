class Solution(object):
    '''
    先得到的hp可以抵消后扣除的hp， 但是先扣除的hp不能被后得到的hp抵消。
    所以如果dfs(row,col)<0, 表示会后得到hp，但是因为后得到的hp不能用来抵消
    先扣除的hp，所以后得到的hp在这里没有意义。
    所以return res if res > 0 else 1要放在dfs里
    '''

    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        self.cache = [[None for _ in dungeon[0]] for _ in dungeon]
        res = self.mem(dungeon, 0, 0)
        return res
        
    def dfs(self, dungeon, row, col):
        '''
        返回从(row,col)到(-1,-1)所需要的最少hp
        '''
        if row == len(dungeon)-1 and col == len(dungeon[0])-1:
            res = 1-dungeon[row][col]
            return res if res > 0 else 1
        right,down = sys.maxsize, sys.maxsize
        if col+1 < len(dungeon[0]):
            right = self.mem(dungeon, row, col+1)
        if row+1 < len(dungeon):
            down = self.mem(dungeon, row+1, col)
        res = min(right, down)-dungeon[row][col]
        return res if res > 0 else 1
    
    def mem(self, dungeon, row, col):
        if self.cache[row][col] == None:
            self.cache[row][col] = self.dfs(dungeon, row, col)
        return self.cache[row][col]
        

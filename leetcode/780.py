class Solution1(object):
    ''' Memory limit exceeded '''
    def reachingPoints(self, sx, sy, tx, ty):
        """
        :type sx: int
        :type sy: int
        :type tx: int
        :type ty: int
        :rtype: bool
        """
        self.cache = [[None for _ in range(max(ty,sy)+1)] for _ in range(max(tx,sx)+1)]
        return self.memo(sx, sy, tx, ty)
        
    def dfs(self, sx, sy, tx, ty):
        if sx == tx and sy == ty:
            return True
        if sx+sy <= ty and self.memo(sx, sx+sy, tx, ty):
            return True
        if sx+sy <= tx and self.memo(sx+sy, sy, tx, ty):
            return True
        return False
    
    def memo(self, sx, sy, tx, ty):
        if self.cache[sx][sy] == None:
            self.cache[sx][sy] = self.dfs(sx, sy, tx, ty)
        return self.cache[sx][sy]

class Solution2(object):
    ''' 
    O(logN) 
    Start from (tx,ty) to (sx,sy)
    '''
    def reachingPoints(self, sx, sy, tx, ty):
        """
        :type sx: int
        :type sy: int
        :type tx: int
        :type ty: int
        :rtype: bool
        """
        if sx > tx or sy > ty:
            return False
        if sx == tx and sy == ty: # found target
            return True
        if tx > ty: # since sx,sy > 0
            tx -= max(1, (tx-sx)//ty) * ty
        else:
            ty -= max(1, (ty-sy)//tx) * tx
        return self.reachingPoints(sx, sy, tx, ty)
            

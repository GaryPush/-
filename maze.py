class Solution:
    
    def buildMaze(self, m, n):
        ''' Generate a maze. '''
        maze = [[1 for _ in range(n)] for _ in range(m)]
        start = (0,0)
        end = (m-1,n-1)
        visited = [[False for _ in range(n)] for _ in range(m)]
        visited[0][0] = True
        maze[0][0] = 0
        winPath = []
        
        self.buildWinPath(maze, start, end, visited, winPath)
        for x,y in winPath:
            self.buildDeadEnds(maze, x, y, visited)
        return maze

    
    def buildDeadEnds(self, maze, x, y, visited):
        ''' Build dead ends from existing path. '''
        moves = self.getMoves(maze, visited, (x,y))
        random.shuffle(moves)
        rand = [i for i in range(1, len(moves)+1)]
        i = random.choice(rand*7+[0]) # complexity of maze is configurable
        moves = moves[:i]
        for i,j in moves:
            maze[i][j] = 0
            visited[i][j] = True
        for i,j in moves:
            self.buildDeadEnds(maze, i, j, visited)


    def buildWinPath(self, maze, start, end, visited, path):
        ''' Use DFS to build a path from start to end. '''
        if start == end:
            return True
        moves = self.getMoves(maze, visited, start)
        random.shuffle(moves)
        for x,y in moves:
            visited[x][y] = True
            maze[x][y] = 0
            path.append((x,y))
            if self.buildWinPath(maze, (x,y), end, visited, path):
                return True
            maze[x][y] = 1
            path.pop()
        return False


    def getMoves(self, maze, visited, current):
        ''' Get available moves. '''
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        x,y = current
        moves = []
        for i,j in directions:
            if 0 <= x+i < len(maze) and 0 <= y+j < len(maze[0]) and not visited[x+i][y+j] and self.isGoodCell(maze, x+i, y+j):
                moves.append((x+i,y+j))
        return moves

    
    def isGoodCell(self, maze, x, y):
        ''' Entering this cell does not create intersection. '''
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        count = 0
        for i,j in directions:
            if 0 <= x+i < len(maze) and 0 <= y+j < len(maze[0]) and maze[x+i][y+j] == 0:
                count += 1
        return count == 1
        
if __name__ == '__main__':
    s = Solution()
    s.buildMaze(10, 10)

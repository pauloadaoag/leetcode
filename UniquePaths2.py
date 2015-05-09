class Solution:
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        y = len(obstacleGrid)
        x = len(obstacleGrid[0])
        pathcount = [[0 for i in xrange(x)] for j in xrange(y)]
        obstacleFound = False
        for x_ in range(x):
            if (obstacleGrid[0][x_]):
                obstacleFound = True
            if (not obstacleFound):
                pathcount[0][x_] = 1
        for x_ in xrange(x):
            for y_ in range(1, y):
                if y_ == 0:
                    top = 0
                elif obstacleGrid[y_ - 1][x_] == 1:
                    top = 0
                else:
                    top = pathcount[y_ - 1][x_]
                if x_ == 0:
                    left = 0
                elif obstacleGrid[y_][x_ - 1] == 1:
                    left = 0
                else:
                    left = pathcount[y_][x_ - 1]
                pathcount[y_][x_] = top + left

                if (obstacleGrid[y_][x_]):
                    pathcount[y_][x_] = 0
        return pathcount[y - 1][x - 1]
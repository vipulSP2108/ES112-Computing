def numCells(grid, n, m):
    yes = 1
    count = 0
    listx = [] 
    for row in range(0, n):
        for col in range(0, m):
            main = grid[row][col]
            if (row != 0):
                if (col != 0):
                    # if (grid[row-1][col-1]>main):
                        listx.append(grid[row-1][col-1])
                if (col != n-1):
                    # if (grid[row-1][col+1]>main):
                        listx.append(grid[row-1][col+1])
                # if (grid[row-1][col]>main):
                listx.append(grid[row-1][col])
            if (row != n-1):
                if (col != 0):
                    # if (grid[row+1][col-1]>main):
                        listx.append(grid[row+1][col-1])
                if (col != n-1):
                    # if (grid[row+1][col+1]>main):
                        listx.append(grid[row+1][col+1])
                # if (grid[row+1][col]>main):
                listx.append(grid[row+1][col])

            if (col != 0):
                if (row != 0):
                    # if (grid[row-1][col-1]>main):        
                        listx.append(grid[row-1][col-1])
                if (row != n-1):
                    # if (grid[row+1][col-1]>main):
                        listx.append(grid[row+1][col-1])
                # if (grid[row][col-1]>main):
                listx.append(grid[row][col-1])
            if (col != n-1):
                if (row != 0):
                    # if (grid[row-1][col+1]>main):
                        listx.append(grid[row-1][col+1])
                if (row != n-1):
                    # if (grid[row+1][col+1]>main):
                        listx.append(grid[row+1][col+1])
                # if (grid[row][col+1]>main):
                listx.append(grid[row][col+1])
            
            listx_count = 0
            for i in listx:
                if (main<=i):
                    listx_count = 0
                    break
                listx_count = 1
            if (listx_count == 1):
                count = count + 1
                
            listx = []
                
    return count

grid = [[1,2,7],[4,5,6],[8,8,9]]
result = numCells(grid, 3, 3)

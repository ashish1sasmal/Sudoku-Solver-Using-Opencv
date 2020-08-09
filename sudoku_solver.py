def find_loc(grid,l):
    for row in range(9):
        for col in range(9):
            if(grid[row][col]== 0):
                l[0]= row
                l[1]= col
                return True
    return False

def safe(grid,row,col,num):
    flag = True
    for i in range(9):
        if grid[row][i] == num:
            flag = False

    for i in range(9):
        if grid[i][col] == num:
            flag = False

    for i in range(3):
        for j in range(3):
            if(grid[(row - row%3) + i][j + (col - col%3)] == num):
                flag = False


    return flag


def main(grid):
    l=[0,0]

    if (not find_loc(grid, l)):
        return True

    row = l[0]
    col = l[1]

    for num in range(1,10):
        if safe(grid,row,col,num):
            grid[row][col] = num

            if(main(grid)):
                return True

            grid[row][col] = 0
    return False



def solve_sudoku(grid):
    if(main(grid)):
        return grid
    else:
        return False

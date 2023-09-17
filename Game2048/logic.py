import random


def start_game():
    """Function to initial grid at the start"""

    matrix = []
    for i in range(4):
        matrix.append([0]*4)
    # print(matrix)
    
    # printing controls for user
    print("Commands are as follows: ")
    print("'W' or 'w': Move Up ")
    print("'S' or 'S': Move Down ")
    print("'A' or 'a': Move Left ")
    print("'D' or 'd': Move Right ")

    # calling the function to add a new 2 in grid after every step
    add_new_2(matrix)
    return matrix


def add_new_2(matrix):
    # choosing a random index for row and column
    # random will probably be 0, 1, 2 because in the last row there is a total value
    # random chỉ là 0, 1, 2 bời vì dòng cuối có giá trị tổng điểm đã đạt được
    row = random.randint(0, 3)
    col = random.randint(0, 3)

    while matrix[row] != 0:
        row = random.randint(0, 3)
        col = random.randint(0, 3)
    
    matrix[row] = 2

    
def get_current_state(matrix):

    # if any cell contains 2048 we have won
    for i in range(4):
        for j in range(4):
            if (matrix[i][j] == 2048): return 'WON!'

    # if we are still left with at least one empty cell game is not yet over
    for i in range(4):
        for j in range(4):
            if (matrix[i][j] == 0):
                return 'Game Not Over!'

    # nếu hiện tại không có ô trống nào nhưng sau khi di chuyển sang trái,
    # phải, lên, xuống nếu có 2 ô được hợp nhất và tạo ra một ô trống
    # thì trò chơi vẫn chưa kết thúc

    # đi xuống dưới, hoặc sang phải
    for i in range(3):
        for j in range(3):
            if (matrix[i][j] == matrix[i+1][j] or matrix[i][j] == matrix[i][j+1]):
                return 'Game Not Over!'

    # hàng cuối đi sang phải
    for j in range(3):
        if (matrix[3][j] == matrix[3][j+1]):
            return 'Game Not Over!'

    # cột cuối đi xuống dưới
    for i in range(3):
        if (matrix[i][3] == matrix[i+1][3]):
            return 'Game Not Over!'
    
    return 'LOST'
    

def compress(matrix):
    # compress: nén

    # bool variable to determine any change happened or not
    changed = False

    # empty grid
    new_matrix = []

    for i in range(4):
        new_matrix.append([0]*4)
    
    # chuyển các mục của mỗi ô đến điểm cực trái từng hàng
    # vòng lặp để duyệt hàng
    for i in range(4):
        pos = 0

        # vòng lặp duyệt qua từng cột của hàng tương ứng
        for j in range(4):

            # nếu ô không trống thì chuyển giá trị của nó sang bên trái của hàng
            if (matrix[i][j] != 0):
                new_matrix[i][pos] = matrix[i][j]

            # nếu j mà không nằm ở vị trí pos thì giá trị sẽ ở pos sẽ thay đổi nên changed = True
            if j != pos:
                changed = True
            
            pos += 1
    
    return new_matrix, changed


def merge(matrix):
    changed = False

    for i in range(4):
        for j in range(3):
            # nếu ô hiện tại có cùng giá trị với ô tiếp theo trong hàng và chúng không trống
            if matrix[i][j] == matrix[i][j+1] and matrix[i][j] != 0:
                matrix[i][j] = matrix[i][j] * 2
                matrix[i][j+1] = 0

                changed = True

    return matrix, changed


def reverse(matrix):
    """Hàm đảo ngược nội dung của mỗi hàng trong ma trận"""
    new_matrix = [] 
    for i in range(4):
        new_matrix.append([])
        
        for j in range(4):
            new_matrix[i].append(matrix[i][3-j])
    
    return new_matrix


def transpose(matrix):
    """Hàm lấy ma trận chuyển vị
    
    Ma trận chuyển vị là hàng thành cột và cột thành hàng
    """
    
    new_matrix = []
    for i in range(4):
        new_matrix.append([])
        for j in range(4):
            new_matrix[i].append(matrix[j][i])
    return new_matrix


def move_left(grid):
    # first compress the grid
    new_grid, changed1 = compress(grid)

    # then merge the cells
    new_grid, changed2 = merge(new_grid)

    changed = changed1 or changed2

    # again compress after merging
    new_grid, temp = compress(grid)

    return new_grid, changed


def move_right(grid):
    # to move right we just reverse the matrix
    new_grid = reverse(grid)

    # then move left
    new_grid, changed = move_left(new_grid)

    # then again reverse matrix will give us desired result
    new_grid = reverse(new_grid)
    return new_grid, changed


def move_up(grid):
    # to move up we just take transpose of matrix
    new_grid = transpose(grid)

    # then move left 
    new_grid, changed = move_left(new_grid)

    # again take transpose will give desired results
    new_grid = transpose(new_grid)
    return new_grid, changed


def move_down(grid):
    # to move down we take transpose
    new_grid = transpose(grid)

    # move right
    new_grid = move_right(new_grid)

    # then again take transpose will give desired results
    new_grid = transpose(new_grid)
    return new_grid, changed



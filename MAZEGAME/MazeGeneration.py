import random


ESC = '\u001b['
RED = '48;2;255;0;0m'
GREEN = '48;2;0;255;0m'
BLUE = '48;2;0;0;255m'
BLACK = '48;2;0;0;0m'
WHITE = '48;2;200;200;200m'
RESET = '\u001b[0m'

class MazeGeneration:
    """"Класс, генерирующий структуру лабиринта."""

    def __init__(self, maze_size = (0, 0)) -> None:
        """
        Конструктор класса.
        params:
            maze_size: размеры лабиринта. 
        """

        self.__maze_size_x = maze_size[0]
        self.__maze_size_y = maze_size[1]
        
    def generate_start_position(self) -> list:
        """Случайная генерация начальной позиции.
        
        Returns:
            x: координата по горизонтали.
            y: координата по вертикали.
            start_side: сторона, где была выбрана координата.
        """

        start_side = random.choice(('top', 'bottom', 'left', 'right'))
        match start_side:
            case 'top' | 'вверх':
                x = random.randrange(1, self.__maze_size_x - 1, 2)
                return x, 0, start_side

            case 'bottom' | 'низ':
                x = random.randrange(1, self.__maze_size_x - 1, 2)
                y = self.__maze_size_y - 1
                return x, y, start_side

            case 'left' | 'лево':
                y = random.randrange(1, self.__maze_size_y-1, 2)
                return 0, y, start_side

            case 'right' | 'право':
                x = self.__maze_size_x - 1
                y = random.randrange(1, self.__maze_size_y-1, 2)
                return x, y, start_side
            
    def generate_maze(self) -> list:
        """Случайная генерация лабиринта.
        
        Returns:
            maze: лабиринт в виде списка списков.
            start_x: координата начальная по горизонтали.
            start_y: координата начальная по вертикали.
            exit_x: координата выхода по горизонтали.
            exit_y: координата выхода по вертикали.
        """

        maze = [['⏹︎' for i in range(self.__maze_size_x)] for j in range(self.__maze_size_y)]

        def checkcoords(x: int, y: int) -> bool:
            """Случайная генерация лабиринта.
        
            Args:
                x: координата по горизонтали.
                y: координата по вертикали.
            """

            if x >= 1 and x < self.__maze_size_x and y >= 1 and y < self.__maze_size_y - 1 and maze[y][x] == '⏹︎':

                return True

            else:

                return False

        start_x, start_y, start_side = self.generate_start_position()
        exit_x, exit_y, exit_side_not_used = self.generate_start_position()
        maze[start_y][start_x] = '♟'

        while True:
            exit_x, exit_y, exit_side = self.generate_start_position()
            if (exit_x, exit_y) != (start_x, start_y):
                break

        maze[exit_y][exit_x] = 'Δ'
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        if start_y == 0:
            list_with_steps = [(start_x, start_y + 1)]
            maze[start_y + 1][start_x] = ' '
        elif start_y == self.__maze_size_y - 1:
            list_with_steps = [(start_x, start_y - 1)]
            maze[start_y - 1][start_x] = ' '
        elif start_x == 0:
            list_with_steps = [(start_x + 1, start_y)]
            maze[start_y][start_x + 1] = ' '
        else:
            list_with_steps = [(start_x - 1, start_y)]
            maze[start_y][start_x - 1] = ' '

        while list_with_steps:
            x, y = list_with_steps[-1]
            neighbors = []

            for dx, dy in directions:
                nx, ny = x + dx*2, y + dy*2
                if checkcoords(nx, ny):
                    neighbors.append((nx, ny))

            if neighbors:
                nx, ny = random.choice(neighbors)
                maze[ny][nx] = ' '
                maze[y + (ny - y)//2][x + (nx - x)//2] = ' '
                list_with_steps.append((nx, ny))
            else:
                list_with_steps.pop()

        return maze, start_x, start_y, exit_x, exit_y
    
    def show_maze(self, maze: list):  
        """Вывод лабиринта в виде матрицы.
        
        Args: 
            maze: случайно сгенерированный лабиринт.
        """

        for i in maze:  
            for j in i:
                if j == '⏹︎':
                    print(ESC + BLACK + ' ', end = ' ')
                    print(RESET, end = '')

                else:
                    print(ESC + WHITE + str(j), end = ' ')
                    print(RESET, end = '')

            print(RESET)
            
#k = MazeGeneration((11, 11))
#maze, start_x, start_y, exit_x, exit_y = k.generate_maze()
#k.show_maze(maze)

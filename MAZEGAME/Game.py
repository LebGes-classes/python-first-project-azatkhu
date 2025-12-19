from MazeGeneration import MazeGeneration
import os

class Game:
    """"Класс, описывающий взаимодействие с игрой."""

    def __init__(self, mazesizex: int, mazesizey: int):
        """
        Конструктор класса.
        params:
            mazesizex: размеры лабиринта по горизонтали. 
            mazesizey: размеры лабиринта по вертикали.
        """

        self.generator = MazeGeneration((mazesizex, mazesizey))
        list_with_data = self.generator.generate_maze()
        self.maze = list_with_data[0]
        self.x = list_with_data[1]
        self.y = list_with_data[2]
        self.finished = False

    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print('----------------------------------------------------')
        print('===================== ЛАБИРИНТ =====================')
        print('----------------------------------------------------')

    def move(self, text):
        x, y = self.x, self.y
        match text:
            case 'w' | 'W': 
                y -= 1
            case 'a' | 'A': 
                x -= 1
            case 's' | 'S': 
                y += 1
            case 'd' | 'D': 
                x += 1

        if self.maze[y][x] != '⏹︎':
            if self.maze[y][x] == 'Δ':
                self.finished = True
            self.maze[self.y][self.x] = ' '
            self.maze[y][x] = '♟'
            self.x, self.y = x, y

    def start_game(self):
        while True:
            self.clear_terminal()
            self.generator.show_maze(self.maze)
            text = input("")
            self.move(text)
            if self.finished:
                self.clear_terminal()
                self.generator.show_maze(self.maze)

                print("Прошёл!")

                break

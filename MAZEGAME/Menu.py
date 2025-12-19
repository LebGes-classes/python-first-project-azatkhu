from Game import Game
import os


class Menu:
    """"Класс, описывающий взаимодействие с пользователем."""
    
    print('----------------------------------------------------')
    print('===================== ЛАБИРИНТ =====================')
    print('----------------------------------------------------')
    print('1 - Начать игру')
    print('2 - Завершить игру')

    user_choice = int(input(''))
    match user_choice:
        case 1:
            choice_to_continue = 1
            k = 7
            while choice_to_continue == 1:
                game = Game(k, k)
                game.start_game()
                
                print('Следующий уровень?')
                print('1 - ДА')
                print('2 - НЕТ')

                choice_to_continue = int(input(''))
                k += 2

            print('Завершено')
        case 2:
            print('Завершено')

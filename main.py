from GUI import GUI
from Level import Level
from Field import Field
from AIPlayer import AIPlayer
import time


def main():
    Level.init_levels()

    new_gui = GUI()
    new_gui.run()

    # level2 = Field([
    #     [3, 9, 4, 12],
    #     [10, 13, 0, 8],
    #     [5, 15, 7, 11],
    #     [1, 14, 2, 6]
    # ])
    #
    # level1 = Field([
    #     [13, 9, 7, 10],
    #     [3, 11, 2, 6],
    #     [0, 15, 14, 5],
    #     [4, 8, 1, 12]
    # ])
    #
    # # player = AIPlayer(level1)
    # # start_time = time.time()  # Начало замера времени
    # # result = player.run_dfs()
    # # end_time = time.time()  # Конец замера времени
    # # print("DFS:")
    # # player.print_path(result)
    # # print(f"Время выполнения DFS: {end_time - start_time:.6f} секунд\n")
    #
    # player = AIPlayer(level1)
    # start_time = time.time()  # Начало замера времени
    # result = player.run_astar()
    # end_time = time.time()  # Конец замера времени
    # print("A*:")
    # player.print_path(result)
    # print(f"Время выполнения A*: {end_time - start_time:.6f} секунд\n")
    #
    # # # Измерение времени выполнения жадного поиска
    # # player = AIPlayer(level1)
    # # start_time = time.time()  # Начало замера времени
    # # result = player.run_greedy()
    # # end_time = time.time()  # Конец замера времени
    # # print("Greedy Search:")
    # # player.print_path(result)
    # # print(f"Время выполнения Greedy Search: {end_time - start_time:.6f} секунд")

if __name__ == '__main__':
    main()

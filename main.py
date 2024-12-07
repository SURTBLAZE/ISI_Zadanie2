import time

from AIPlayer import AIPlayer
from Field import Field


def main():
    # Ініціалізуємо кілька полів для перевірки роботи алгоритму
    field1 = Field([
        [7, 2, 4],
        [5, 0, 6],
        [8, 3, 1]
    ])  # solvable

    field2 = Field([
        [1, 2, 0],
        [3, 4, 5],
        [6, 7, 8]
    ])  # solvable

    field3 = Field([
        [1, 2, 3, 0],
        [4, 5, 6, 7],
        [8, 9, 10, 11],
        [12, 13, 14, 15]
    ])  # solvable

    field3_wrong = Field([
        [2, 1, 3, 0],
        [4, 5, 6, 7],
        [8, 9, 10, 11],
        [12, 13, 14, 15]
    ])  # Поле 4x4, нерозв'язне через неправильну кількість інверсій

    # Виводимо поле
    field1.display()

    player = AIPlayer(field1)

    dfs_start_time = time.time()
    dfs_field = player.run_dfs()
    dfs_end_time = time.time()

    AIPlayer.print_path(dfs_field)


    astar_start_time = time.time()
    astar_field = player.run_astar()
    astar_end_time = time.time()

    AIPlayer.print_path(astar_field)


    greedy_start_time = time.time()
    greedy_field = player.run_greedy()
    greedy_end_time = time.time()

    AIPlayer.print_path(greedy_field)

    print(f"dfs: {dfs_end_time - dfs_start_time:.8f} sec")
    print(f"astar: {astar_end_time - astar_start_time:.8f} sec")
    print(f"greedy: {greedy_end_time - greedy_start_time:.8f} sec")


if __name__ == '__main__':
    main()

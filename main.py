from field import Field
from AI_Player import AI_Player

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

# Виводимо поле field3
field3.display()

# Ініціалізуємо гравця AI_Player із розв'язним полем field3
player = AI_Player(field3)

# Отримуємо та виводимо шлях до розв'язку з використанням DFS
player.get_dfs_path()
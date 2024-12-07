from Field import Field


class Utils:

    @staticmethod
    def heuristic(field: Field) -> int:
        # Обчислення евристичної функції (мангеттенської відстані)
        size = field.get_size()  # Розмір поля
        manhattan_distance = 0  # Ініціалізація мангеттенської відстані

        # Перебір всіх клітинок поля
        for row in range(size):
            for col in range(size):
                value = field.get_field()[row][col]
                if value == 0:  # Пропускаємо порожню клітинку
                    continue

                # Визначаємо цільову позицію для кожного числа
                target_row, target_col = divmod(value, size)
                # Додаємо мангеттенську відстань для поточної клітинки
                manhattan_distance += abs(row - target_row) + abs(col - target_col)

        # Повертаємо загальну мангеттенську відстань
        return manhattan_distance

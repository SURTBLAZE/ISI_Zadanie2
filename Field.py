class Field:
    def __init__(self, field):
        # Перевіряємо, чи поле має розмір 3x3 або 4x4
        if len(field) != 3 and len(field) != 4 or not all(len(row) == 3 for row in field) and not all(len(row) == 4 for row in field):
            raise ValueError("size must be 3x3 or 4x4")
        self.field = field
        self.last_field = None  # Зберігає посилання на попередній стан поля
        self.size = len(field)  # Розмір поля (3 або 4)

    def get_size(self) -> int:
        # Повертає розмір поля
        return self.size

    def get_field(self):
        # Повертає поточний стан поля
        return self.field

    def get_last_field(self):
        # Повертає попередній стан поля
        return self.last_field

    def set_last_field(self, last_field):
        # Встановлює попередній стан поля
        self.last_field = last_field

    def display(self):
        # Виводить поле у форматованому вигляді
        max_width = len(str(self.size ** 2 - 1))  # Максимальна ширина для вирівнювання цифр
        separator = " | " if self.size == 3 else "   |   "  # Роздільник залежить від розміру поля

        for row in self.field:
            # Форматуємо рядок, вирівнюючи кожен елемент за максимальним розміром
            formatted_row = separator.join(f"{num:>{max_width}}" for num in row)
            print(formatted_row)

        print()

    def is_solved(self) -> bool:
        # Перевіряє, чи поле знаходиться у вирішеному стані
        value = 0
        for row in range(self.size):
            for column in range(self.size):
                if self.field[row][column] != value:
                    return False
                value += 1
        return True

    def is_solvable(self) -> bool:
        # Перевіряє, чи поле розв'язне
        # Перетворюємо двовимірний масив у одномірний, виключаючи 0
        flattened = [num for row in self.field for num in row if num != 0]

        # Рахуємо кількість інверсій
        inversions = 0
        for i in range(len(flattened)):
            for j in range(i + 1, len(flattened)):
                if flattened[i] > flattened[j]:
                    inversions += 1

        # Знаходимо позицію порожньої клітинки (0)
        empty_row = next(row for row in range(self.size) if 0 in self.field[row])

        # Для поля з непарною кількістю рядків
        if self.size % 2 == 1:
            return inversions % 2 == 0  # Розв'язне, якщо кількість інверсій парна

        # Для поля з парною кількістю рядків
        else:
            # Порожня клітинка знаходиться на "парному рядку знизу", якщо (size - empty_row - 1) парне
            is_empty_on_even_row_from_bottom = (self.size - empty_row - 1) % 2 == 0
            print()
            if is_empty_on_even_row_from_bottom:
                return inversions % 2 == 1  # Розв'язне, якщо кількість інверсій непарна
            else:
                return inversions % 2 == 0  # Розв'язне, якщо кількість інверсій парна

    def generate_moves(self) ->  list:
        # Генерує всі можливі ходи для поточного стану поля
        for i in range(self.size):
            for j in range(self.size):
                if self.field[i][j] == 0:
                    empty_row, empty_col = i, j  # Знаходимо позицію порожньої клітинки
                    break

        directions = [
            (1, 0),  # вниз
            (0, 1),  # вправо
            (0, -1),  # вліво
            (-1, 0)  # вверх
        ]

        new_fields = []

        for dr, dc in directions:
            new_row, new_col = empty_row + dr, empty_col + dc

            # Перевіряємо, чи нові координати знаходяться в межах поля
            if 0 <= new_row < self.size and 0 <= new_col < self.size:

                # Копіюємо поточний стан поля
                new_field = [row[:] for row in self.field]

                # Міняємо місцями порожню клітинку і сусідню клітинку
                new_field[empty_row][empty_col] = new_field[new_row][new_col]
                new_field[new_row][new_col] = 0

                # Створюємо новий об'єкт поля
                new_field_obj = Field(new_field)
                new_field_obj.set_last_field(self)  # Зберігаємо посилання на поточне поле
                new_fields.append(new_field_obj)

        return new_fields  # Повертає список нових станів поля

    def get_tuple(self) -> tuple:
        return tuple(tuple(row) for row in self.field)
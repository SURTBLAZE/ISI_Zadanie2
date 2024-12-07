from field import Field

class AI_Player:
    def __init__(self, input_field):
        # Ініціалізуємо гравця з полем
        # Перевіряємо, чи поле не None та чи воно розв'язне
        if input_field is None or not input_field.is_solvable():
            raise ValueError("AI_Player: input_field is None or is unsolvable")
        self.field = input_field  # Початкове поле
        self.visited = set()  # Множина відвіданих станів

    def dfs(self) -> Field:
        # Реалізуємо пошук у глибину (DFS), щоб знайти розв'язок головоломки
        stack = [self.field]  # Стек для збереження станів
        self.visited = set()  # Оновлюємо множину відвіданих станів

        while stack:
            # Виймаємо поточне поле зі стеку
            current_field = stack.pop()

            # Перевіряємо, чи є поле розв'язаним
            if current_field.is_solved():
                print("Puzzle solved!")
                current_field.display()  # Виводимо розв'язане поле
                return current_field  # Повертаємо розв'язок

            # Перетворюємо поточне поле в кортеж для перевірки у visited
            current_field_tuple = tuple(tuple(row) for row in current_field.get_field())

            # Пропускаємо поле, якщо воно вже було відвідане
            if current_field_tuple in self.visited:
                continue

            # Додаємо поточне поле у множину відвіданих
            self.visited.add(current_field_tuple)

            # Генеруємо можливі нові стани поля та додаємо їх у стек
            for new_field in current_field.generate_moves():
                stack.append(new_field)

        # Якщо розв'язок не знайдено
        print("No solution found.")
        return None

    def get_dfs_path(self):
        # Отримує шлях від початкового стану до розв'язку
        path = []  # Список для збереження послідовності полів
        current_field = self.dfs()  # Виконуємо DFS і отримуємо розв'язане поле

        # Відстежуємо шлях до розв'язку за посиланнями на попередні стани
        while current_field is not None:
            path.append(current_field)  # Додаємо поточний стан у шлях
            current_field = current_field.get_last_field()  # Переходимо до попереднього стану

        path.reverse()  # Реверсуємо шлях, щоб отримати послідовність від початкового стану до розв'язку

        # Виводимо кількість кроків і сам шлях
        print(f"Total steps: {len(path) - 1}")  # Виводимо кількість кроків (без початкового стану)
        for step, field in enumerate(path):
            print(f"Step {step}:")  # Виводимо номер кроку
            field.display()  # Виводимо стан поля на цьому кроці
from overrides import overrides

from Algorithm import Algorithm
from Field import Field


class DFS(Algorithm):
    def __init__(self, field):
        self.field = field
        self.visited = set()

    @overrides
    def run(self) -> Field | None:
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
            current_field_tuple = current_field.get_tuple()

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

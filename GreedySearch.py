import heapq

from overrides import overrides

from Algorithm import Algorithm
from Field import Field
from Utils import Utils


class GreedySearch(Algorithm):
    def __init__(self, field: Field):
        # Ініціалізація об'єкта GreedySearch з початковим полем
        self.field = field
        self.goal = self.generate_goal_state()  # Генеруємо цільове поле
        self.counter = 0  # Лічильник для унікальності елементів у купі

    def generate_goal_state(self):
        # Генерація цільового поля для розв'язку (наприклад, порядковий порядок чисел)
        goal = []
        value = 1
        for i in range(self.field.get_size()):
            row = []
            for j in range(self.field.get_size()):
                row.append(value)
                value += 1
            goal.append(row)
        goal[-1][-1] = 0  # Остання клітинка — порожня (0)
        return goal

    @overrides
    def run(self) -> Field | None:
        # Основний цикл пошуку
        open_set = []  # Черга для відкритих елементів
        visited = set()  # Множина для відвіданих полів

        # Додаємо початковий елемент у купу з нульовою вартістю
        heapq.heappush(open_set, (0, self.counter, self.field))
        self.counter += 1  # Збільшуємо лічильник

        # Додаємо початкове поле в множину відвіданих
        visited.add(self.field.get_tuple())

        # Основний цикл пошуку
        while open_set:
            # Витягуємо елемент з найменшою евристичною оцінкою (за принципом жадібного пошуку)
            _, _, current_state = heapq.heappop(open_set)

            # Перевіряємо, чи знайдено рішення
            if current_state.is_solved():
                print("Puzzle solved!")  # Якщо знайдено, виводимо повідомлення
                current_state.display()  # Виводимо рішення
                return current_state  # Повертаємо вирішене поле

            # Генеруємо нові стани (сусіди)
            for neighbor in current_state.generate_moves():
                neighbor_tuple = neighbor.get_tuple()  # Перетворюємо сусіда в кортеж

                # Якщо сусід ще не відвідувався, додаємо його в множину відвіданих і в чергу
                if neighbor_tuple not in visited:
                    visited.add(neighbor_tuple)  # Додаємо сусіда до множини відвіданих
                    # Оцінюємо сусіда за допомогою евристичної функції
                    heapq.heappush(open_set, (Utils.heuristic(neighbor), self.counter, neighbor))
                    self.counter += 1  # Збільшуємо лічильник для унікальності елементів

        # Якщо не знайдено рішення
        print("No solution found.")
        return None

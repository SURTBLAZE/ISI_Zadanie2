import heapq

from overrides import overrides

from Algorithm import Algorithm
from Field import Field
from Utils import Utils


class Astar(Algorithm):
    def __init__(self, field: Field):
        # Ініціалізація об'єкта Astar з початковим полем
        self.field = field
        self.counter = 0  # Лічильник для унікальності елементів у купі

    @overrides
    def run(self) -> Field | None:
        # Початкові налаштування для пошуку
        open_set = []  # Черга для відкритих елементів
        g_scores = {self.field.get_tuple(): 0}  # Словник для зберігання відстаней від старту
        visited = set()  # Множина для відвіданих полів

        # Додаємо початковий елемент у купу з нульовою вартістю
        heapq.heappush(open_set, (0, self.counter, self.field))
        self.counter += 1  # Збільшуємо лічильник

        # Основний цикл пошуку
        while open_set:
            # Витягуємо елемент з найменшою вартістю (f_score)
            _, _, current_field = heapq.heappop(open_set)

            # Перевіряємо, чи знайдено рішення
            if current_field.is_solved():
                print("Puzzle solved!")  # Якщо знайдено, виводимо повідомлення
                current_field.display()  # Виводимо рішення
                return current_field  # Повертаємо вирішене поле

            # Обробляємо сусідів поточного поля
            self.process_neighbors(current_field, open_set, g_scores, visited)

        # Якщо не знайдено рішення
        print("No solution found.")
        return None

    def process_neighbors(self, current_field, open_set, g_scores, visited):
        # Обробка сусідів поточного поля
        current_field_tuple = current_field.get_tuple()  # Перетворюємо поле в кортеж для збереження
        visited.add(current_field_tuple)  # Додаємо поле в множину відвіданих

        # Перебираємо всі можливі сусіди (ходи)
        for neighbor in current_field.generate_moves():
            neighbor_tuple = neighbor.get_tuple()  # Перетворюємо сусіда в кортеж

            # Якщо сусід уже відвіданий, пропускаємо його
            if neighbor_tuple in visited:
                continue

            # Обчислюємо новий g_score для сусіда
            tentative_g_score = g_scores[current_field_tuple] + 1

            # Якщо цей сусід не відвідувався або знайдено кращий шлях до нього
            if neighbor_tuple not in g_scores or tentative_g_score < g_scores[neighbor_tuple]:
                # Встановлюємо попереднє поле для цього сусіда
                neighbor.set_last_field(current_field)
                g_scores[neighbor_tuple] = tentative_g_score  # Оновлюємо g_score
                # Обчислюємо f_score для сусіда (g_score + евристична оцінка)
                f_score = tentative_g_score + Utils.heuristic(neighbor)
                # Додаємо сусіда в чергу з новим f_score
                heapq.heappush(open_set, (f_score, self.counter, neighbor))
                self.counter += 1  # Збільшуємо лічильник для унікальності

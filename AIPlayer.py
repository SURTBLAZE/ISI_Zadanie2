from Astar import Astar
from DFS import DFS
from Field import Field
from GreedySearch import GreedySearch


class AIPlayer:
    def __init__(self, field: Field):
        if field is None or not field.is_solvable():
            raise ValueError("AI_Player: field is None or is unsolvable")

        self.field = field

    def run_astar(self) -> Field | None:
        astar = Astar(self.field)
        return astar.run()

    def run_dfs(self) -> Field | None:
        dfs = DFS(self.field)
        return dfs.run()

    def run_greedy(self) -> Field | None:
        greedy = GreedySearch(self.field)
        return greedy.run()

    @staticmethod
    def print_path(field: Field):
        path = []

        while field is not None:
            path.append(field)
            field = field.get_last_field()

        path.reverse()

        print(f"Total steps: {len(path) - 1}")
        for step, current_field in enumerate(path):
            print(f"Step {step}:")
            current_field.display()

    @staticmethod
    def get_path(field: Field):
        path = []

        while field is not None:
            path.append(field)
            field = field.get_last_field()

        path.reverse()
        return path

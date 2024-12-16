import heapq

from overrides import overrides

from Algorithm import Algorithm
from Field import Field
from Utils import Utils


class GreedySearch(Algorithm):
    def __init__(self, field: Field):
        self.field = field
        self.goal = self.generate_goal_state()
        self.counter = 0

    def generate_goal_state(self):
        goal = []
        value = 1
        for i in range(self.field.get_size()):
            row = []
            for j in range(self.field.get_size()):
                row.append(value)
                value += 1
            goal.append(row)
        goal[-1][-1] = 0
        return goal

    @overrides
    def run(self) -> Field | None:
        open_set = []  # Queue for open elements
        visited = set()  # Set for visited fields

        # Add the initial element to the heap with zero cost
        heapq.heappush(open_set, (0, self.counter, self.field))
        self.counter += 1

        # Add the initial field to the visited set
        visited.add(self.field.get_tuple())

        while open_set:
            # Extract the element with the lowest heuristic score (greedy search approach)
            _, _, current_state = heapq.heappop(open_set)

            if current_state.is_solved():
                print("Puzzle solved!")
                current_state.display()
                return current_state

            # Generate new states (neighbors)
            for neighbor in current_state.generate_moves():
                neighbor_tuple = neighbor.get_tuple()  # Convert the neighbor to a tuple

                # If the neighbor hasn't been visited yet, add it to the visited set and the queue
                if neighbor_tuple not in visited:
                    visited.add(neighbor_tuple)

                    heapq.heappush(open_set, (Utils.heuristic(neighbor), self.counter, neighbor))
                    self.counter += 1

        # If no solution is found
        print("No solution found.")
        return None


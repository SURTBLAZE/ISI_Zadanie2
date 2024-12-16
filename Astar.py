import heapq

from overrides import overrides

from Algorithm import Algorithm
from Field import Field
from Utils import Utils


class Astar(Algorithm):
    def __init__(self, field: Field):
        self.field = field
        self.counter = 0

    @overrides
    def run(self) -> Field | None:
        open_set = []  # Queue for open elements
        g_scores = {self.field.get_tuple(): 0}  # Dictionary to store distances from the start
        visited = set()  # Set for visited fields

        heapq.heappush(open_set, (0, self.counter, self.field))
        self.counter += 1

        while open_set:
            # Extract the element with the lowest cost (f_score)
            _, _, current_field = heapq.heappop(open_set)

            if current_field.is_solved():
                print("Puzzle solved!")
                current_field.display()
                return current_field

            # Process neighbors of the current field
            self.process_neighbors(current_field, open_set, g_scores, visited)

        # If no solution is found
        print("No solution found.")
        return None

    def process_neighbors(self, current_field, open_set, g_scores, visited):
        # Processing neighbors of the current field
        current_field_tuple = current_field.get_tuple()  # Convert the field to a tuple for storage
        visited.add(current_field_tuple)  # Add the field to the visited set

        # Iterate through all possible neighbors (moves)
        for neighbor in current_field.generate_moves():
            neighbor_tuple = neighbor.get_tuple()  # Convert the neighbor to a tuple

            # If the neighbor has already been visited, skip it
            if neighbor_tuple in visited:
                continue

            tentative_g_score = g_scores[current_field_tuple] + 1

            # If this neighbor has not been visited or a better path to it has been found
            if neighbor_tuple not in g_scores or tentative_g_score < g_scores[neighbor_tuple]:
                # Set the previous field for this neighbor
                neighbor.set_last_field(current_field)
                g_scores[neighbor_tuple] = tentative_g_score

                f_score = tentative_g_score + Utils.heuristic(neighbor)

                heapq.heappush(open_set, (f_score, self.counter, neighbor))
                self.counter += 1

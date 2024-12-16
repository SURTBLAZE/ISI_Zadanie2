from overrides import overrides

from Algorithm import Algorithm
from Field import Field


class DFS(Algorithm):
    def __init__(self, field):
        self.field = field
        self.visited = set()

    @overrides
    def run(self) -> Field | None:
        stack = [self.field]  # Stack to store states
        self.visited = set()  # Update the set of visited states

        while stack:
            current_field = stack.pop()

            if current_field.is_solved():
                print("Puzzle solved!")
                current_field.display()
                return current_field

            # Convert the current field to a tuple for checking in visited
            current_field_tuple = current_field.get_tuple()

            if current_field_tuple in self.visited:
                continue

            # Add the current field to the visited set
            self.visited.add(current_field_tuple)

            # Generate possible new states of the field and add them to the stack
            for new_field in current_field.generate_moves():
                stack.append(new_field)

        # If no solution is found
        print("No solution found.")
        return None

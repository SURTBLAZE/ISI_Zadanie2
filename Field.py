class Field:
    def __init__(self, field):
        # Check if the field is 3x3 or 4x4 in size
        if len(field) != 3 and len(field) != 4 or not all(len(row) == 3 for row in field) and not all(
                len(row) == 4 for row in field):
            raise ValueError("size must be 3x3 or 4x4")

        self.field = field
        self.last_field = None
        self.size = len(field)

    def get_size(self) -> int:
        return self.size

    def get_field(self):
        return self.field

    def get_last_field(self):
        return self.last_field

    def set_last_field(self, last_field):
        self.last_field = last_field

    def display(self):
        # Displays the field in a formatted manner
        max_width = len(str(self.size ** 2 - 1))
        separator = " | " if self.size == 3 else "   |   "

        for row in self.field:
            # Format the row, aligning each element to the maximum width
            formatted_row = separator.join(f"{num:>{max_width}}" for num in row)
            print(formatted_row)

        print()

    def is_solved(self) -> bool:
        value = 0
        for row in range(self.size):
            for column in range(self.size):
                if self.field[row][column] != value:
                    return False
                value += 1
        return True

    def is_solvable(self) -> bool:
        # Convert the 2D array to a 1D array, excluding 0
        flattened = [num for row in self.field for num in row if num != 0]

        # Count the number of inversions
        inversions = 0
        for i in range(len(flattened)):
            for j in range(i + 1, len(flattened)):
                if flattened[i] > flattened[j]:
                    inversions += 1

        # Find the position of the empty cell (0)
        empty_row = next(row for row in range(self.size) if 0 in self.field[row])

        # For fields with an odd number of rows
        if self.size % 2 == 1:
            return inversions % 2 == 0  # Solvable if the number of inversions is even

        # For fields with an even number of rows
        else:
            # The empty cell is on an "even row from the bottom" if (size - empty_row - 1) is even
            is_empty_on_even_row_from_bottom = (self.size - empty_row - 1) % 2 == 0
            print()
            if is_empty_on_even_row_from_bottom:
                return inversions % 2 == 1  # Solvable if the number of inversions is odd
            else:
                return inversions % 2 == 0  # Solvable if the number of inversions is even

    def generate_moves(self) -> list:
        # Generates all possible moves for the current state of the field
        for i in range(self.size):
            for j in range(self.size):
                if self.field[i][j] == 0:
                    empty_row, empty_col = i, j  # Find the position of the empty cell
                    break

        directions = [
            (1, 0),  # down
            (0, 1),  # right
            (0, -1),  # left
            (-1, 0)  # up
        ]

        new_fields = []

        for dr, dc in directions:
            new_row, new_col = empty_row + dr, empty_col + dc

            # Check if the new coordinates are within the bounds of the field
            if 0 <= new_row < self.size and 0 <= new_col < self.size:
                # Copy the current state of the field
                new_field = [row[:] for row in self.field]

                # Swap the empty cell with the neighboring cell
                new_field[empty_row][empty_col] = new_field[new_row][new_col]
                new_field[new_row][new_col] = 0

                # Create a new field object
                new_field_obj = Field(new_field)
                new_field_obj.set_last_field(self)  # Store the reference to the current field
                new_fields.append(new_field_obj)

        return new_fields  # Return the list of new field states

    def get_tuple(self) -> tuple:
        return tuple(tuple(row) for row in self.field)

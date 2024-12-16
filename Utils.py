from Field import Field


class Utils:

    @staticmethod
    def heuristic(field: Field) -> int:
        size = field.get_size()
        manhattan_distance = 0

        for row in range(size):
            for col in range(size):
                value = field.get_field()[row][col]
                if value == 0:
                    continue

                target_row, target_col = divmod(value, size)
                manhattan_distance += abs(row - target_row) + abs(col - target_col)

        return manhattan_distance

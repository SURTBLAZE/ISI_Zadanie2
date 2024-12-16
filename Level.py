from Field import Field


class Level:
    levels = []

    @staticmethod
    def init_levels():
        level1 = Field([
            [7, 2, 4],
            [5, 0, 6],
            [8, 3, 1]
        ])
        level2 = Field([
            [6, 2, 1],
            [7, 3, 8],
            [5, 4, 0]
        ])
        level3 = Field([
            [2, 3, 5],
            [4, 6, 7],
            [8, 1, 0]
        ])
        level4 = Field([
            [4, 3, 7],
            [2, 8, 5],
            [1, 6, 0]
        ])
        level5 = Field([
            [7, 6, 4],
            [0, 3, 5],
            [2, 8, 1]
        ])

        level6 = Field([
            [13, 9, 7, 10],
            [3, 11, 2, 6],
            [0, 15, 14, 5],
            [4, 8, 1, 12]
        ])
        level7 = Field([
            [7, 14, 4, 0],
            [2, 8, 1, 6],
            [3, 9, 5, 13],
            [15, 11, 10, 12]
        ])
        level8 = Field([
            [3, 9, 4, 12],
            [10, 13, 0, 8],
            [5, 15, 7, 11],
            [1, 14, 2, 6]
        ])
        level9 = Field([
            [8, 7, 13, 5],
            [3, 4, 12, 1],
            [9, 15, 14, 6],
            [2, 10, 11, 0]
        ])
        level10 = Field([
            [1, 10, 2, 3],
            [4, 5, 6, 7],
            [8, 9, 0, 11],
            [12, 13, 14, 15]
        ])

        Level.levels = [level1, level2, level3, level4, level5,
                        level6, level7, level8, level9, level10]

import tkinter as tk
from tkinter import messagebox
import time
from Field import Field
from AIPlayer import AIPlayer


class GUI:
    def __init__(self, field: Field):
        self.field = field
        self.player = AIPlayer(field)

    def run(self):
        root = tk.Tk()
        root.title("Lloydova 8-ička (15-tka)")

        canvas = tk.Canvas(root, width=300, height=300, bg="white")
        canvas.pack(pady=10)

        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="DFS", command=lambda: self.on_solve("DFS", canvas)).grid(row=0, column=0, padx=5)
        tk.Button(button_frame, text="Astar", command=lambda: self.on_solve("Astar", canvas)).grid(row=0, column=1, padx=5)
        tk.Button(button_frame, text="GreedySearch", command=lambda: self.on_solve("GreedySearch", canvas)).grid(row=0,
                                                                                                            column=2,
                                                                                                            padx=5)

        self.draw_grid(canvas, self.field.get_field())

        root.mainloop()

    def draw_grid(self,canvas, state):
        canvas.delete("all")
        rows, cols = len(state), len(state[0])
        cell_size = 100


        canvas.config(width=cols * cell_size, height=rows * cell_size)

        for i in range(rows):
            for j in range(cols):
                x1, y1 = j * cell_size, i * cell_size
                x2, y2 = x1 + cell_size, y1 + cell_size
                value = state[i][j]
                if value != 0:
                    canvas.create_rectangle(x1, y1, x2, y2, fill="lightblue", outline="black")
                    canvas.create_text((x1 + x2) // 2, (y1 + y2) // 2, text=str(value), font=("Arial", 24))

    def on_solve(self, method, canvas):
        path = self.solve_puzzle(method)
        if not path:
            messagebox.showerror("Error", f"no solution from {method}")
            return

        moves = len(path)
        speed = max(1, moves // 10)
        self.animate_solution(canvas, path, speed)

    def animate_solution(self, canvas, path, speed):
        for state in path:
            self.draw_grid(canvas, state.get_field())
            canvas.update()
            time.sleep(1 / speed)

    def solve_puzzle(self, method):
        if method == "DFS":
            dfs_field = self.player.run_dfs()
            return AIPlayer.get_path(dfs_field)
        elif method == "Astar":
            dfs_field = self.player.run_astar()
            return AIPlayer.get_path(dfs_field)
        elif method == "GreedySearch":
            dfs_field = self.player.run_greedy()
            return AIPlayer.get_path(dfs_field)
        return []
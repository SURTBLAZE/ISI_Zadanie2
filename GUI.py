import time
import tkinter as tk
from tkinter import messagebox

from AIPlayer import AIPlayer
from Field import Field


class GUI:
    def __init__(self, field: Field):
        self.field = field
        self.player = AIPlayer(field)
        self.is_stopped = False
        self.is_algorithm_running = False

    def run(self):
        root = tk.Tk()
        root.title("Lloydova 8-ička (15-tka)")

        frame = tk.Frame(root)
        frame.pack(padx=30, pady=(30, 40))

        canvas = tk.Canvas(frame, bg="#CD7F32")
        canvas.pack()

        button_frame = tk.Frame(root)
        button_frame.pack(pady=(0, 30))

        button_frame.grid_columnconfigure(2, minsize=50)

        (tk.Button(button_frame,
                   text="Reset", bg="green", fg="white", padx=7, pady=3,
                   command=lambda: self.reset_grid(canvas))
         .grid(row=0, column=0, padx=5))

        (tk.Button(button_frame,
                   text="Stop", bg="red", fg="white", padx=7, pady=3,
                   command=lambda: self.stop_algorithm())
         .grid(row=0, column=1, padx=5))

        (tk.Button(button_frame, text="DFS", padx=7, pady=3, bg="#CBCBCB",
                   command=lambda: self.on_solve("DFS", canvas))
         .grid(row=0, column=3, padx=5))

        (tk.Button(button_frame, text="Astar", padx=7, pady=3, bg="#CBCBCB",
                   command=lambda: self.on_solve("Astar", canvas))
         .grid(row=0, column=4, padx=5))

        (tk.Button(button_frame, text="GreedySearch", padx=7, pady=3, bg="#CBCBCB",
                   command=lambda: self.on_solve("GreedySearch", canvas))
         .grid(row=0, column=5, padx=5))

        self.draw_grid(canvas, self.field.get_field())

        root.mainloop()

    def stop_algorithm(self):
        if self.is_algorithm_running:
            self.is_stopped = True
            self.is_algorithm_running = False

    def reset_grid(self, canvas):
        if not self.is_algorithm_running:
            self.draw_grid(canvas, self.field.get_field())

    def draw_grid(self, canvas, state):
        canvas.delete("all")
        rows, cols = len(state), len(state[0])
        cell_size = 150
        frame_padding = 20

        canvas.config(width=cols * cell_size + 2 * frame_padding,
                      height=rows * cell_size + 2 * frame_padding)

        for i in range(rows):
            for j in range(cols):
                x1, y1 = j * cell_size + frame_padding, i * cell_size + frame_padding
                x2, y2 = x1 + cell_size, y1 + cell_size
                value = state[i][j]
                if value != 0:
                    canvas.create_rectangle(
                        x1, y1, x2, y2,
                        fill="#FFFDD0", outline="black"
                    )
                    canvas.create_text(
                        (x1 + x2) // 2, (y1 + y2) // 2,
                        text=str(value), font=("Arial", 24), fill="darkblue"
                    )
                else:
                    canvas.create_rectangle(x1, y1, x2, y2, fill="#FFF8F1", outline="black")

    def on_solve(self, method, canvas):
        if self.is_algorithm_running:
            return

        path = self.solve_puzzle(method)
        if not path:
            messagebox.showerror("Error", f"no solution from {method}")
            return

        moves = len(path)
        speed = max(1, moves // 10)
        self.animate_solution(canvas, path, speed)

    def animate_solution(self, canvas, path, speed):
        for state in path:
            if self.is_stopped:
                self.is_stopped = False
                return

            self.is_algorithm_running = True

            self.draw_grid(canvas, state.get_field())
            canvas.update()
            time.sleep(1 / speed)

        self.is_algorithm_running = False

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

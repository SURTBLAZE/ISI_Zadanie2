import tkinter as tk


class MenuGUI:
    def __init__(self):
        self.selected_level = None

    def run_menu(self, root):
        self.selected_level = tk.IntVar()

        menu_frame = tk.Frame(root)
        menu_frame.grid(row=0, column=0, padx=20, pady=20)

        tk.Label(menu_frame, text="Choose Level:", font=("Arial", 14)).grid(row=0, column=0, columnspan=6, pady=(10,20))

        for i in range(1, 11):
            tk.Button(menu_frame,
                      text=f"Level {i}",
                      bg="#CBCBCB", padx=20, pady=20,
                      command=lambda level=i: self.select_level(level)
                      ).grid(row=(i - 1) // 5 + 1, column=(i - 1) % 5, padx=10, pady=10)

        root.wait_variable(self.selected_level)
        menu_frame.destroy()

    def select_level(self, level):
        self.selected_level.set(level)

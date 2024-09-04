"""
File: fractal_tree.py
Author: Rodolfo Lopez and Justin de Sousa 
Date: 3/14/2020
Description: Displays fractal tree
"""

import math
import tkinter as tk


class FractalTree:
    def __init__(self):
        """Initialize the fractal object."""

        # Useful variables for calculations
        self.size = 400
        self.length_scale = 0.58
        self.angle_scale = math.pi / 5
        self.current_levels_of_recursion = 1

        # Creates window, canvas, control frame, buttons
        self.window = tk.Tk()
        self.window.title("Fractal Tree")

        self.canvas = tk.Canvas(
            self.window,
            width=self.size,
            height=self.size,
            borderwidth=1,
            relief="solid",
        )
        self.canvas.grid(row=1, column=1)

        self.control_frame = tk.Frame(self.window, width=self.size, height=50)
        self.control_frame.grid(row=2, column=1)
        self.control_frame.grid_propagate(False)

        self.advance_button = tk.Button(
            self.control_frame, text="Advance", command=self.advance
        )
        self.advance_button.grid(row=1, column=1)

        self.reset_button = tk.Button(
            self.control_frame, text="Reset", command=self.reset
        )
        self.reset_button.grid(row=1, column=2)

        self.quit_button = tk.Button(self.control_frame, text="Quit", command=self.quit)
        self.quit_button.grid(row=1, column=3)

        # Evenly spaces rows and columns
        self.control_frame.grid_rowconfigure(1, weight=1)
        self.control_frame.grid_columnconfigure(1, weight=1)
        self.control_frame.grid_columnconfigure(2, weight=1)
        self.control_frame.grid_columnconfigure(3, weight=1)

        # Calls function to draw initial branch onto the canvas
        self.create_branch(
            self.size // 2,
            self.size,
            self.size // 2,
            2 * self.size / 3,
        )

        tk.mainloop()

    def advance(self):
        """Advance one level of recursion"""
        self.current_levels_of_recursion += 1
        self.canvas.delete("line")
        self.draw_fractal(
            self.size / 2,
            self.size,
            self.size / 3,
            math.pi / 2,
            self.current_levels_of_recursion,
        )

    def reset(self):
        """Reset to 0 levels of recursion"""
        self.canvas.delete("all")
        self.current_levels_of_recursion = 1
        self.create_branch(self.size // 2, self.size, self.size // 2, 2 * self.size / 3)

    def quit(self):
        """Quit the program"""
        self.window.destroy()

    def create_branch(self, x1, y1, x2, y2):
        """Draws branch with given coordinates"""
        self.canvas.create_line(x1, y1, x2, y2, tag="line")

    def draw_fractal(
        self, child_start_x, child_start_y, child_length, angle, levels_of_recursion
    ):
        """This recursive function draws a fractal tree and the fractal tree's depth depends on the current levels
        of recursion that are added by clicking the advance button. The funciton takes in the parameters that
        specify the x and y coordinates of where a particular fractal tree's branch begins. It also takes in
        the angle that the branch makes with the horizonatal line to the side of it as well as the depth or
        levels of recursion in order to handle the advance buton event."""
        # Base Case
        if levels_of_recursion == 0:
            self.create_branch(
                self.size // 2, self.size, self.size // 2, 2 * self.size / 3
            )
        # Recursive Case
        else:
            # Lowers fractal tree depth
            levels_of_recursion -= 1

            # Calculates where the branch ends and where the next branch will begin
            child_end_x = child_start_x + int(math.cos(angle) * child_length)
            child_end_y = child_start_y - int(math.sin(angle) * child_length)

            # Draws the child branches
            self.create_branch(child_start_x, child_start_y, child_end_x, child_end_y)

            # Recursive call for right branches
            self.draw_fractal(
                child_end_x,
                child_end_y,
                child_length * self.length_scale,
                angle + self.angle_scale,
                levels_of_recursion,
            )

            # Recursive call for left branches
            self.draw_fractal(
                child_end_x,
                child_end_y,
                child_length * self.length_scale,
                angle - self.angle_scale,
                levels_of_recursion,
            )


if __name__ == "__main__":
    FractalTree()

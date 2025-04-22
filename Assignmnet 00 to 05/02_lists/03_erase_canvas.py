                                    ## Problem Statement

# Implement an 'eraser' on a canvas. 
# The canvas consists of a grid of blue 'cells' which are drawn as rectangles on the screen. 
# We then create an eraser rectangle which, when dragged around the canvas, sets all of the 
# rectangles it is in contact with to white.

                                    ## Starter Code

# ```bash
# def main():
#     print("Delete this line and write your code here! :)")


# # This provided line is required at the end of
# # Python file to call the main() function.
# if __name__ == '__main__':
#     main()
# ```

                                    ## Solution

"""
This program implements an 'eraser' on a canvas. 

The canvas consists of a grid of blue 'cells' which are drawn 
as rectangles on the screen. We then create an eraser rectangle
which, when dragged around the canvas, sets all of the rectangles 
it is in contact with to white.
"""

import tkinter as tk

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

class EraserApp:
    def __init__(self, root):
        self.canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg='white')
        self.canvas.pack()
        self.cells = []

        self.draw_grid()
        self.eraser = self.canvas.create_rectangle(0, 0, ERASER_SIZE, ERASER_SIZE, fill='pink')
        self.canvas.bind("<Motion>", self.move_eraser)

    def draw_grid(self):
        for row in range(0, CANVAS_HEIGHT, CELL_SIZE):
            for col in range(0, CANVAS_WIDTH, CELL_SIZE):
                rect = self.canvas.create_rectangle(
                    col, row, col + CELL_SIZE, row + CELL_SIZE, fill='blue', outline='black'
                )
                self.cells.append(rect)

    def move_eraser(self, event):
        x, y = event.x, event.y
        self.canvas.coords(self.eraser, x, y, x + ERASER_SIZE, y + ERASER_SIZE)

        overlapping = self.canvas.find_overlapping(x, y, x + ERASER_SIZE, y + ERASER_SIZE)
        for item in overlapping:
            if item != self.eraser:
                self.canvas.itemconfig(item, fill='white')


def main():
    root = tk.Tk()
    root.title("Canvas Eraser")
    app = EraserApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()

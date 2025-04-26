from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.root = Tk()
        self.root.title = "Maze Solver"
        self.canvas = Canvas(self.root, {"bg": "white"})
        self.canvas.pack()
        self.win_running = False

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.win_running = True
        while self.win_running:
            self.redraw()
        
    def close(self):
        self.win_running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

class Point:
    def __init__(self):
        self.x = 0
        self.y = 0

class Line:
    def __init__(self, ):
        pass

def main():
    win = Window(800, 600)
    win.wait_for_close()

if __name__ == "__main__":
    main()
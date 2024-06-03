from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Line, Bezier
from random import randint


class CurvyStrokeGrid(GridLayout):
    def __init__(self, **kwargs):
        super(CurvyStrokeGrid, self).__init__(**kwargs)
        self.cols = 10  # Number of columns in the grid
        self.rows = 10  # Number of rows in the grid
        self.spacing = [2, 2]  # Spacing between grid cells
        self.bind(size=self.update_size)  # Bind update_size to handle size changes

    def update_size(self, instance, value):
        # Calculate the cell size whenever the grid size changes
        self.cell_width = self.width / self.cols
        self.cell_height = self.height / self.rows
        self.draw_curvy_stroke()

    def draw_curvy_stroke(self):
        with self.canvas:
            Bezier(points=self.generate_random_points(), segment_lines=100)

    def generate_random_points(self):
        # Generate random control points for a Bézier curve
        points = []
        for i in range(self.cols):
            x = self.x + i * self.cell_width + randint(-100, 100)
            y = self.y + i * self.cell_height + randint(-100, 100)
            points.extend([x, y])
        return points


class CurvyStrokeApp(App):
    def build(self):
        return CurvyStrokeGrid()


if __name__ == "__main__":
    CurvyStrokeApp().run()

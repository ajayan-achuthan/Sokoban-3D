import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ListProperty
from kivy.uix.screenmanager import ScreenManager, Screen

kivy.require('2.1.0')

class SokobanGame(GridLayout):
    def __init__(self, **kwargs):
        super(SokobanGame, self).__init__(**kwargs)
        self.cols = 5
        self.rows = 5
        self.level_data = [
            "#####",
            "#@$.#",
            "#   #",
            "#   #",
            "#####"
        ]
        self.build_board()

    def build_board(self):
        self.clear_widgets()
        for row in range(self.rows):
            for col in range(self.cols):
                if self.level_data[row][col] == '@':
                    self.add_widget(Button(text='P', background_color=(1, 1, 0, 1)))
                elif self.level_data[row][col] == '$':
                    self.add_widget(Button(text='B', background_color=(1, 0.5, 0, 1)))
                elif self.level_data[row][col] == '.':
                    self.add_widget(Button(text='G', background_color=(1, 1, 0, 1)))
                else:
                    self.add_widget(Button(background_color=(0.5, 0.5, 0.5, 1)))

    def move_player(self, direction):
        x, y = self.player_pos
        if direction == 'up':
            y -= 1
        elif direction == 'down':
            y += 1
        elif direction == 'left':
            x -= 1
        elif direction == 'right':
            x += 1

        if 0 <= x < self.cols and 0 <= y < self.rows:
            if [x, y] in self.boxes:
                self.move_box(x, y, direction)
            else:
                self.player_pos = [x, y]
                self.build_board()

    def move_box(self, x, y, direction):
        box_index = self.boxes.index([x, y])
        if direction == 'up':
            new_pos = [x, y - 1]
        elif direction == 'down':
            new_pos = [x, y + 1]
        elif direction == 'left':
            new_pos = [x - 1, y]
        elif direction == 'right':
            new_pos = [x + 1, y]

        if 0 <= new_pos[0] < self.cols and 0 <= new_pos[1] < self.rows and new_pos not in self.boxes:
            self.boxes[box_index] = new_pos
            self.player_pos = [x, y]
            self.build_board()

class SokobanApp(App):
    def build(self):
        root = GridLayout(cols=1)
        game = SokobanGame()
        root.add_widget(game)

        buttons = GridLayout(cols=4, size_hint_y=None, height=50)
        buttons.add_widget(Button(text='Up', on_press=lambda x: game.move_player('up')))
        buttons.add_widget(Button(text='Left', on_press=lambda x: game.move_player('left')))
        buttons.add_widget(Button(text='Right', on_press=lambda x: game.move_player('right')))
        buttons.add_widget(Button(text='Down', on_press=lambda x: game.move_player('down')))

        root.add_widget(buttons)
        return root

if __name__ == '__main__':
    SokobanApp().run()

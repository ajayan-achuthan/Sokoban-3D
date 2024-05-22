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
        self.direction = {'up':[-1,0],'down':[1,0],'left':[0,-1],'right':[0,1]}
        self.cols = 5
        self.rows = 5
        self.level_data = [
            "#####",
            "#@$.#",
            "#   #",
            "#   #",
            "#####"
        ]
        for i in range(len(self.level_data)):
            self.level_data[i] = list(self.level_data[i])
        self.player_pos = [0,0]
        for i in range(len(self.level_data)):
            for j in range(len(self.level_data[i])):
                if self.level_data[i][j] == '@':
                    self.player_pos = [i,j]
        self.build_board()

    def build_board(self):
        self.clear_widgets()
        for row in range(self.rows):
            for col in range(self.cols):
                if self.level_data[row][col] == '#':
                    self.add_widget(Button(text='#', background_color=(1, 1, 0, 1)))
                elif self.level_data[row][col] == '@':
                    self.add_widget(Button(text='P', background_color=(1, 1, 0, 1)))
                elif self.level_data[row][col] == '$':
                    self.add_widget(Button(text='B', background_color=(1, 0.5, 0, 1)))
                elif self.level_data[row][col] == '.':
                    self.add_widget(Button(text='G', background_color=(1, 1, 0, 1)))
                else:
                    self.add_widget(Button(background_color=(0.5, 0.5, 0.5, 1)))

    def move_player(self, direction):
        x, y = self.player_pos
        prevx,prevy = x,y
        x, y = x+self.direction[direction][0], y+self.direction[direction][1]

        if 0 <= x < self.rows and 0 <= y < self.cols:
            if self.level_data[x][y] == '$':
                self.move_box(x, y, direction)
            else:
                self.player_pos = [x,y]
                self.level_data[prevx][prevy] =' '
                self.level_data[x][y] ='@'
                self.build_board()

    def move_box(self, x, y, direction):
        prevx,prevy = x,y
        x, y = x+self.direction[direction][0], y+self.direction[direction][1]

        if 0 <= x < self.rows and 0 <= y < self.cols and self.level_data[x][y] != '$':
            self.level_data[x][y] = '$'
            self.player_pos = [prevx,prevy]
            self.level_data[prevx][prevy] ='@'
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

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color

class SokobanGame(Widget):
    def __init__(self, **kwargs):
        super(SokobanGame, self).__init__(**kwargs)
        self.cols = 5
        self.rows = 5
        self.cell_size = 50
        self.init_game()
        
    def init_game(self):
        self.clear_widgets()
        self.canvas.clear()
        self.level_data = [
            "#####",
            "#@$.#",
            "#   #",
            "#@  #",
            "#####"
        ]
        
        with self.canvas:
            for row in range(self.rows):
                for col in range(self.cols):
                    cell = self.level_data[row][col]
                    x = col * self.cell_size
                    y = (self.rows - row - 1) * self.cell_size
                    if cell == "#":
                        Color(0, 0, 0)
                    elif cell == "@":
                        Color(0, 0, 1)
                    elif cell == "$":
                        Color(1, 0, 0)
                    elif cell == ".":
                        Color(0, 1, 0)
                    else:
                        Color(1, 1, 1)
                    Rectangle(pos=(x, y), size=(self.cell_size, self.cell_size))
                    
class MainScreen(Screen):
    pass

class GameScreen(Screen):
    def __init__(self, **kwargs):
        super(GameScreen, self).__init__(**kwargs)
        self.game = SokobanGame()
        self.add_widget(self.game)

class SokobanApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(GameScreen(name='game'))
        return sm

    def new_game(self, instance):
        self.root.current = 'game'

if __name__ == '__main__':
    SokobanApp().run()

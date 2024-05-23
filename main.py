from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
import kivy
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ListProperty,StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen
import queue
from game import SokobanGame
from utils import level_finder
from kivy.clock import mainthread

class MainScreen(Screen):
    pass

class NewGameScreen(Screen):
    pass

class LevelScreen(Screen):
    @mainthread
    def on_enter(self):
        for i in range(10): 
            app = App.get_running_app()
            button = Button(text=str(i),size_hint_y= None, height= 50,on_release=lambda a:app.show_game(i+1))
            #button.bind()
            self.ids.grid.add_widget(button)

class GameScreen(Screen):
    rows = NumericProperty()
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        pass
    
    def update_game(self, rows,cols,matrix):
        self.rows = rows
        self.cols = cols
        self.matrix = matrix
        root = GridLayout(cols=1)
        game = SokobanGame(rows=rows,cols=cols,matrix=matrix)
        root.add_widget(game)

        buttons = GridLayout(cols=4, size_hint_y=None, height=50)
        buttons.add_widget(Button(text='Up', on_press=lambda x: game.move(0,-1, True)))
        buttons.add_widget(Button(text='Left', on_press=lambda x: game.move(-1,0, True)))
        buttons.add_widget(Button(text='Right', on_press=lambda x: game.move(1,0, True)))
        buttons.add_widget(Button(text='Down', on_press=lambda x: game.move(0,1, True)))

        root.add_widget(buttons)
        self.add_widget(root)

class SokobanApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.collection = ''
        self.rows = 0
        self.cols = 0
        self.matrix = ''
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(NewGameScreen(name='new_game'))
        sm.add_widget(LevelScreen(name='levels'))
        sm.add_widget(GameScreen(name='game'))
        return sm

    def new_game(self, instance):
        self.root.current = 'new_game'

    def show_levels(self, instance, collection):
        self.collection = collection
        self.root.current = 'levels'

    def back_to_main(self, instance):
        self.root.current = 'main'

    def back_to_new_game(self, instance):
        self.root.current = 'new_game'

    def show_game(self,level):
        self.width,self.height,self.matrix =level_finder(self.collection,level-1)
        
        self.root.current = 'game'
        self.root.get_screen('game').update_game(self.height,self.width,self.matrix)

if __name__ == '__main__':
    SokobanApp().run()

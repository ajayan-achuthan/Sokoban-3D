import kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ListProperty,StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import mainthread
from kivy.storage.jsonstore import JsonStore
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.graphics import Color,RoundedRectangle
import queue
from game import SokobanGame
import utils #available_collections

from kivy.core.text import LabelBase
LabelBase.register(name='clearsans', fn_regular='assets/fonts/ClearSans-Bold.ttf')

class MainScreen(Screen):
    pass

class NewGameScreen(Screen):
    def on_enter(self):
        self.ids.collection_grid.clear_widgets()
        slcs = utils.available_collections()
        app = App.get_running_app()
        for i in slcs:
            complete,total = utils.count_completed(i)
            button = Button(text=f"{i} {complete}/{total}",size_hint_y= None, height= 50,on_release=lambda a,curr=i:app.show_levels(self,curr))
            self.ids.collection_grid.add_widget(button)

class LevelScreen(Screen):
    collection_name = StringProperty()
    def on_enter(self):
        app = App.get_running_app()
        self.collection_name = app.collection.upper()
        self.ids.level_grid.clear_widgets()
        for i in range(app.no_levels):
            bg_color = utils.is_completed(app.collection,i+1)
            button = Button(text=str(i+1),size_hint_y= None, height= 50, background_color=bg_color,on_release=lambda a,curr=i:app.show_game(curr+1))
            self.ids.level_grid.add_widget(button)

class GameScreen(Screen):
    collection_name = StringProperty()
    level_name = StringProperty()
    moves = NumericProperty(0)
    pushes = NumericProperty(0)
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        pass
    def update_game(self, rows,cols,matrix):
        app = App.get_running_app()
        self.collection_name = app.collection
        self.level_name = str(app.level)
        self.ids.game_grid.clear_widgets()
        self.game_square = AnchorLayout(anchor_x= 'center',anchor_y= 'center')
        self.game = SokobanGame(rows=rows,cols=cols,matrix=matrix)
        self.game_square.add_widget(self.game)
        self.game_square.bind(size=self.on_size)
        self.ids.game_grid.add_widget(self.game_square)
        
    def update_moves(self,moves,pushes):
        self.moves = moves
        self.pushes =pushes
    def on_size(self, *args):
        self.game.size_hint = (None,None)
        self.game.size = (min(self.game_square.size),min(self.game_square.size))

class GameCompleted(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        root = GridLayout(cols=1)
        app = App.get_running_app()
        buttons = GridLayout(cols=3, size_hint_y=None, height=50)
        buttons.add_widget(Button(text='Next level', on_press=lambda x: app.show_game(app.level+1)))
        buttons.add_widget(Button(text='Restart', on_press=lambda x: app.show_game(app.level)))
        buttons.add_widget(Button(text='Menu', on_press=lambda x: app.back_to_show_levels()))
        root.add_widget(buttons)
        self.add_widget(root)

class SokobanApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(NewGameScreen(name='new_game'))
        sm.add_widget(LevelScreen(name='levels'))
        sm.add_widget(GameScreen(name='game'))
        sm.add_widget(GameCompleted(name='complete'))
        return sm

    def new_game(self, instance):
        self.root.current = 'new_game'

    def show_levels(self, instance, collection):
        self.collection = collection
        self.no_levels = utils.count_levels(collection)
        self.root.current = 'levels'

    def show_game(self,level):
        self.level = level
        self.width,self.height,self.matrix =utils.level_finder(self.collection,level-1)
        self.root.current = 'game'
        self.root.get_screen('game').update_game(self.height,self.width,self.matrix)

    def show_completed(self):
        utils.add_completed(self.collection,self.level)
        self.root.current = 'complete'

    def back_to_main(self, instance):
        self.root.current = 'main'

    def back_to_new_game(self, instance):
        self.root.current = 'new_game'

    def back_to_show_levels(self):
        self.root.current = 'levels'

if __name__ == '__main__':
    Window.size = (375, 800)
    SokobanApp().run()

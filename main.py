import kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ListProperty,StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import mainthread
from kivy.storage.jsonstore import JsonStore
from kivy.uix.boxlayout import BoxLayout
import queue
from game import SokobanGame
import utils #available_collections

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
    def update_game(self, rows,cols,matrix):
        self.rows = rows
        self.cols = cols
        self.matrix = matrix
        app = App.get_running_app()
        box=BoxLayout(size_hint = (1,1))
        root = GridLayout(cols=1,padding = [30,30,30,30])
        print(root.size,root.height,root.width,"dfsf")
        game = SokobanGame(rows=rows,cols=cols,matrix=matrix)
        root.add_widget(game)
        buttons = GridLayout(cols=7, size_hint_y=None, height=50)
        buttons.add_widget(Button(text='Up', on_press=lambda x: game.move(0,-1, True)))
        buttons.add_widget(Button(text='Left', on_press=lambda x: game.move(-1,0, True)))
        buttons.add_widget(Button(text='Right', on_press=lambda x: game.move(1,0, True)))
        buttons.add_widget(Button(text='Down', on_press=lambda x: game.move(0,1, True)))
        buttons.add_widget(Button(text='Undo', on_press=lambda x: game.unmove()))
        buttons.add_widget(Button(text='Reset', on_press=lambda x: game.reset()))
        buttons.add_widget(Button(text='Back', on_press=lambda x: app.back_to_show_levels()))
        root.add_widget(buttons)
        box.add_widget(root)
        self.add_widget(box)

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
        pass
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

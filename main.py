from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

class MainScreen(Screen):
    pass

class NewGameScreen(Screen):
    pass

class LevelScreen(Screen):
    pass

class SokobanApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(NewGameScreen(name='new_game'))
        sm.add_widget(LevelScreen(name='levels'))
        return sm

    def new_game(self, instance):
        self.root.current = 'new_game'

    def show_levels(self, instance):
        self.root.current = 'levels'

    def back_to_main(self, instance):
        self.root.current = 'main'

    def back_to_new_game(self, instance):
        self.root.current = 'new_game'

if __name__ == '__main__':
    SokobanApp().run()

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class GameInterface(GridLayout):
    def __init__(self, **kwargs):
        super(GameInterface, self).__init__(**kwargs)
        self.cols = 2

        # Title label
        self.add_widget(Label(text='2048', font_size='40sp'))

        # Score display
        self.score_label = Label(text='SCORE: 0')
        self.add_widget(self.score_label)

        # Best score display
        self.best_label = Label(text='BEST: 0')
        self.add_widget(self.best_label)

        # New game button
        new_game_button = Button(text='New Game', size_hint=(None, None), width=200, height=50)
        new_game_button.bind(on_press=self.new_game)
        self.add_widget(new_game_button)

    def new_game(self, instance):
        # Logic for starting a new game goes here
        pass

class GameApp(App):
    def build(self):
        return GameInterface()

if __name__ == '__main__':
    GameApp().run()

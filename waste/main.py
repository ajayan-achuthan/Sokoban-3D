from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')

        # Create three buttons
        btn1 = Button(text="Button 1")
        btn1.bind(on_press=lambda instance: self.go_to_result('Button 1'))
        layout.add_widget(btn1)

        btn2 = Button(text="Button 2")
        btn2.bind(on_press=lambda instance: self.go_to_result('Button 2'))
        layout.add_widget(btn2)

        btn3 = Button(text="Button 3")
        btn3.bind(on_press=lambda instance: self.go_to_result('Button 3'))
        layout.add_widget(btn3)

        self.add_widget(layout)

    def go_to_result(self, button_text):
        # Passing the button text as an argument to the result screen
        self.manager.current = 'result'
        self.manager.get_screen('result').update_result(button_text)

class ResultScreen(Screen):
    def __init__(self, **kwargs):
        super(ResultScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        
        self.label = Label(text="You have pressed button: ")
        self.layout.add_widget(self.label)
        
        self.add_widget(self.layout)
    
    def update_result(self, button_text):
        self.label.text = f"You have pressed button: {button_text}"

class MyApp(App):
    def build(self):
        sm = ScreenManager(transition=SlideTransition())
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(ResultScreen(name='result'))
        return sm

if __name__ == '__main__':
    MyApp().run()

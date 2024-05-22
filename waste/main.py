from kivy.app import App
from kivy.lang import Builder

kv_string = """
BoxLayout:
    orientation: 'vertical'
    pos: root.pos
    size: root.size

    GridLayout:
        rows: 2
        spacing: 5
        padding: 5
""" + ''.join(["""
        Button:
            text: "X{0}"
            on_press: root.X({0})
""".format(i) for i in range(6)])

class MyApp(App):
    def build(self):
        w = Builder.load_string(kv_string)
        return w

if __name__ == '__main__':
    MyApp().run()
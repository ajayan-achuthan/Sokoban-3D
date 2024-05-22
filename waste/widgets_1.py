import kivy
kivy.require('1.10.0')
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.uix.boxlayout import MDBoxLayout

class MyLabel(MDBoxLayout):
    admin = StringProperty()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print("admin", len(self.admin),"gffg")
        if self.admin == "user":
            self.md_bg_color = "green"
        else:
            self.md_bg_color = "red"
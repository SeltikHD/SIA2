import kivy
from kivy.app import App
from kivy.uix.label import Label

kivy.require('2.3.0')


class SIIA(App):
    def build(self):
        return Label(text='Hello, World!')


siia = SIIA()
siia.run()

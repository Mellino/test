import kivy
from kivy.uix.label import Label
from kivy.app import App


class App(App):
    def build(self):
        return Label(text="hello world")

if __name__ == "__main__":
    App().run()
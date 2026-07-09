from kivy.app import App

from src.ui.screens.home_screen import HomeScreen


class OgarniaczApp(App):
    def build(self):
        return HomeScreen()
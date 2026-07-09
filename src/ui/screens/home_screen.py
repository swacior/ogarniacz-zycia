from kivy.uix.label import Label


class HomeScreen(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = "🏠 Ekran główny Ogarniacza Życia"
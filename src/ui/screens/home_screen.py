from src.core.user_manager import current_user
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class HomeScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.orientation = "vertical"
        self.spacing = 10
        self.padding = 20

        self.add_widget(
            Label(
                text=f"👋 Dzień dobry {current_user.name}"
                )
        )

        self.add_widget(
            Label(text="📅 Dzisiejszy dzień")
        )

        self.add_widget(
            Label(text="🌤️ Pogoda\n22°C, słonecznie")
        )

        self.add_widget(
            Label(text="📋 Plan na dziś\nBrak zadań")
        )

        self.add_widget(
            Label(
                text="🤖 Sugestia Ogarniacza\n"
                     "Pamiętaj o odpoczynku!"
            )
        )

        self.voice_button = Button(
            text="🎤 Nagraj wiadomość",
            size_hint=(1, 0.2)
        )

        self.voice_button.bind(
            on_press=self.voice_clicked
        )

        self.add_widget(self.voice_button)

    def voice_clicked(self, instance):
        print("Nagrywanie głosówki...")
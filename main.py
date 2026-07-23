from kivy.app import App
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        return Button(
            text="Xin chào Chau Ho!",
            font_size=30
        )

MyApp().run()

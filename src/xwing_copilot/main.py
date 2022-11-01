from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, NoTransition


class XwingCopilot(App):
    def build(self):
        self.icon = r"assests/icon.png"
        sm = ScreenManager(transition=NoTransition())
        return sm


if __name__ == "__main__":
    app = XwingCopilot()
    app.run()

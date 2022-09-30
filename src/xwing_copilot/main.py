from kivy.app import App
from kivy.uix.label import Label


class XwingCopilot(App):
    def build(self):
        self.icon = "assests/icon.png"
        return Label(text="X-Wing Copilot")


if __name__ == "__main__":
    app = XwingCopilot()
    app.run()

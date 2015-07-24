from kivy.app import App
from kivy.uix.widget import Widget


class VideoWidget(Widget):
    pass


class VideoApp(App):
    def build(self):
        return VideoWidget()


if __name__ == '__main__':
    VideoApp().run()
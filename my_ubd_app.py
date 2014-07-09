
from kivy.app import App
from kivy.clock import Clock
from ubd.ubd_app import MainUBD


class MyMainUBDWindow(MainUBD):
    def __init__(self):
        super(MyMainUBDWindow, self).__init__('my_app.xml')
        #Clock.schedule_once(self.after)


class MyUBDApp(App):
    def build(self):
        return MyMainUBDWindow()


if __name__ == '__main__':
    MyUBDApp().run()

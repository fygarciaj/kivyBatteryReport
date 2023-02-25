from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.utils import platform


if platform=='android':
    from android.permissions import request_permissions, Permission
    request_permissions([Permission.INTERNET])

if platform != "android":
    Window.size = (300, 600)

Builder.load_file('kvs/main.kv')  

class WindowManager(ScreenManager):
    pass


class MainScreen(Screen):
    pass

class MyApp(MDApp):
    def __init__(self, **kwargs) -> None:
        self.title="Battery Status"
        super().__init__(**kwargs)
    
    def build(self):
        self.wm = WindowManager()
        self.theme_cls.theme_style = 'Light'
        self.theme_cls.primary_palete = 'Teal'
        screens = [
            MainScreen(name='main'),
        ]
        for screen in screens:
            self.wm.add_widget(screen)
        return self.wm

if __name__=="__main__":
    MyApp().run()
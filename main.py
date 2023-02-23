import builtins
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang import Builder


Window.size= (600, 800)

Builder.load_file('kvs/main.kv')

class MyApp(MDApp):
    def build(self):
        return 

if __name__=="__main__":
    MyApp().run()
from kivy.lang import Builder
from kivymd.app import MDApp

from view_ui import text_ui


class StudentApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        screen = Builder.load_string(text_ui)
        return screen


    def navigation_draw(self):
        print("shiiiiit")


StudentApp().run()

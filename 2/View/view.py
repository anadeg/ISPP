from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton

from view_ui import text_ui, enter_path, enter_path_button, path_dialog
from screens_ui import screens, screens2


# class ShowStudentsScreen(Screen):
#     pass
#
#
# class InputPathScreen(Screen):
#     pass


class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    drawer = ObjectProperty()


class TestNavigationApp(MDApp):
    def build(self):
        return Builder.load_string(screens2)

# sm = ScreenManager()
# sm.add_widget(ShowStudentsScreen(name='table'))
# sm.add_widget(InputPathScreen(name='input path'))
#
#
# class StudentApp(MDApp):
#     def build(self):
#         # self.screen = Screen()
#         #
#         # self.theme_cls.primary_palette = "Green"
#         # # self.entering_button = MDRectangleFlatButton(
#         # #                                             text="show",
#         # #                                             pos_hint={"center_x": 0.5, "center_y": 0.4},
#         # #                                             on_release=self.show_path
#         # #                                             )
#         # self.enter_path_button = Builder.load_string(enter_path_button)
#         # self.enter_path = Builder.load_string(enter_path)
#         #
#         # self.screen.add_widget(self.enter_path)
#         # self.screen.add_widget(self.enter_path_button)
#         # return self.screen
#         screen = Builder.load_string(screens)
#         return screen
#
#     def show_path(self, obj):
#         input_path_text = self.enter_path.text
#         self.dialog = Builder.load_string(path_dialog)
#         self.screen.add_widget(self.dialog)
#         self.dialog.open()
#
#     def close_dialog(self, obj):
#         self.dialog.dismiss()


TestNavigationApp().run()

from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.dialog import MDDialog

from screens_ui import content_of_entering_path, using_navigation
from generate_table import generate_table


class Content(BoxLayout):
    pass


class ContentNavigationDrawer(BoxLayout):
    pass


class MainApp(MDApp):
    def build(self):
        screen = Screen()
        navigation = Builder.load_string(using_navigation)
        # input_path_dialog = Builder.load_string(content_of_entering_path)
        # return Builder.load_string(content_of_entering_path)
        data_table = MDDataTable(
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            size_hint=(0.95, 0.8),
            use_pagination=True,
            column_data=[
                ("Name", dp(60)),
                ("Group", dp(25)),
                ("Sick", dp(25)),
                ("Absent", dp(25)),
                ("Other", dp(25)),
            ]
        )
        data = generate_table(60)
        data_table.row_data = data

        screen.add_widget(data_table)
        screen.add_widget(navigation)
        # screen.add_widget(input_path_dialog)
        return screen

    def open_file_name_dialog(self):
        content = Builder.load_string(content_of_entering_path)
        self.file_name_dialog = MDDialog(
            title='enter file name',
            content_cls=Content(),
            type="custom",
            buttons=[
                MDRectangleFlatButton(
                    text='enter',
                    theme_text_color='Custom',
                    text_color=self.theme_cls.primary_color,
                    on_release=self.close_enter_path_dialog
                )
            ]
        )
        self.file_name_dialog.open()


    def close_enter_path_dialog(self, obj):
        self.file_name_dialog.dismiss()


MainApp().run()

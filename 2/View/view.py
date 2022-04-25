from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.dialog import MDDialog

from Controller.controller import Controller
from Model.model import Model

from screens_ui import content_of_entering_path, using_navigation
from generate_table import generate_table


class Content(BoxLayout):
    pass


class ContentNavigationDrawer(BoxLayout):
    pass


class StudentDataDialog(BoxLayout):
    pass


class MainApp(MDApp):
    # None to run without conflicts
    def __init__(self, controller=None, **kwargs):
        super().__init__(**kwargs)
        self.controller = controller

    def build(self):
        screen = Screen()
        navigation = Builder.load_string(using_navigation)
        self.data_table = MDDataTable(
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            size_hint=(0.95, 0.8),
            use_pagination=True,
            column_data=[
                ("Full Name", dp(60)),
                ("Group", dp(25)),
                ("Sick", dp(25)),
                ("Absent", dp(25)),
                ("Other", dp(25)),
            ]
        )
        data = generate_table(60)
        data_table.row_data = data

        screen.add_widget(self.data_table)
        screen.add_widget(navigation)
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
                    on_release=self.get_students_table_by_path
                )
            ]
        )
        self.file_name_dialog.open()

    # view calls controller
    # controller gives model path and asks to give table
    # controller returns table
    # controller gives table as MDDataTable argument to view
    def get_students_table_by_path(self, obj):
        self.file_name_dialog.dismiss()
        path = self.file_name_dialog.content_cls.ids.file.text
        data = self.controller.download_students(path)
        self.data_table.row_data = data

    # view gives controller filter settings
    # use all not empty fields as filter modes
    # controller gives model modes
    # model returns filtered data (as new table)
    # controller gives data to view MDDialog
    def get_filtered_students(self, *args):
        pass

    # calls filter through controller
    # controller returns table of student
    # shows it in MDDialog
    def show_filtered_students(self, *args):
        pass

    # calls filter through controller
    # controller returns table of student
    # counts deleted students
    def show_deleted_students(self, *args):
        pass

    # view gives data to controller
    # controller asks model to make student
    # student is added to table
    def create_new_student(self, *args):
        pass

    def close_enter_path_dialog(self, obj):
        self.file_name_dialog.dismiss()


def main():
    m = Model()
    c = Controller(m)
    MainApp(c).run()


if __name__ == "__main__":
    main()


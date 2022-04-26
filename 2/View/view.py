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

from screens_ui import using_navigation


class Content(BoxLayout):
    pass


class ContentNavigationDrawer(BoxLayout):
    pass


class StudentDataDialog(BoxLayout):
    pass


class DialogTable(BoxLayout):
    pass


class AddStudentDialog(BoxLayout):
    pass


class MainApp(MDApp):
    # None to run without conflicts
    def __init__(self, controller=None, **kwargs):
        super().__init__(**kwargs)
        self.controller = controller
        self.data_table = ObjectProperty()
        self.file_name_dialog = ObjectProperty()
        self.input_student_dialog = ObjectProperty()

    def build(self):
        screen = Screen()
        navigation = Builder.load_string(using_navigation)
        self.data_table = MDDataTable(
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            size_hint=(0.95, 0.8),
            use_pagination=True,
            rows_num=10,
            column_data=[
                ("Full Name", dp(60)),
                ("Group", dp(25)),
                ("Sick", dp(25)),
                ("Absent", dp(25)),
                ("Other", dp(25)),
            ]
        )

        screen.add_widget(self.data_table)
        screen.add_widget(navigation)
        return screen

    def open_file_name_dialog(self, function_name):
        self.file_name_dialog = MDDialog(
            title='Enter File Name',
            content_cls=Content(),
            type="custom",
            buttons=[
                MDRectangleFlatButton(
                    text='Enter',
                    theme_text_color='Custom',
                    text_color=self.theme_cls.primary_color,
                    # on_release=self.get_students_table_by_path
                    on_release=function_name
                )
            ]
        )
        self.file_name_dialog.open()

    def open_input_student_dialog(self, function_name):
        self.input_student_dialog = MDDialog(
            title='Input Student Info',
            content_cls=StudentDataDialog(),
            type="custom",
            buttons=[
                MDRectangleFlatButton(
                    text='Enter',
                    theme_text_color='Custom',
                    text_color=self.theme_cls.primary_color,
                    # on_release=self.get_students_table_by_path
                    on_release=function_name
                )
            ]
        )
        self.input_student_dialog.open()

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
    def get_filtered_students(self, obj):
        self.input_student_dialog.dismiss()

        name = self.input_student_dialog.content_cls.ids.input_full_name.text
        group = self.input_student_dialog.content_cls.ids.input_group.text
        sick = self.input_student_dialog.content_cls.ids.input_sick.text
        absent = self.input_student_dialog.content_cls.ids.input_absent.text
        other = self.input_student_dialog.content_cls.ids.input_other.text

        return self.controller.filters(name, group, sick, absent, other)

    # calls filter through controller
    # controller returns table of student
    # shows it in MDDialog
    def show_filtered_students(self, obj):
        data = self.get_filtered_students(obj)
        layout = BoxLayout(
            orientation="vertical",
            spacing='2dp',
            padding='5dp',
            size_hint_y=None,
            height='400dp',
        )
        table = MDDataTable(
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            use_pagination=True,
            rows_num=7,
            column_data=[
                ("Full Name", dp(60)),
                ("Group", dp(25)),
                ("Sick", dp(25)),
                ("Absent", dp(25)),
                ("Other", dp(25)),
            ]
        )

        layout.add_widget(table)

        self.student_dialog = MDDialog(
            title='Filtered Students',
            size_hint=(.9, .9),
            content_cls=layout,
            type="custom",
            buttons=[
                MDRectangleFlatButton(
                    text='Close',
                    theme_text_color='Custom',
                    text_color=self.theme_cls.primary_color,
                    on_release=lambda _: self.student_dialog.dismiss()
                )
            ]
        )

        table.row_data = data
        self.student_dialog.open()

    # calls filter through controller
    # controller returns table of student
    # counts deleted students
    def show_deleted_students(self, obj):
        data = self.get_filtered_students(obj)
        indexes = self.controller.delete_students(data)
        # new_table = self.controller.get_student_table()

        for index in indexes:
            self.data_table.remove_row(self.data_table.row_data[index])

        if data:
            text = f"{len(data)} students were deleted"
        else:
            text = "No student was deleted"

        # self.data_table.row_data = new_table
        self.deleted_student_dialog = MDDialog(
            title="Deleted Information",
            text=text,
            buttons=[
                MDRectangleFlatButton(
                    text='Close',
                    theme_text_color='Custom',
                    text_color=self.theme_cls.primary_color,
                    on_release=lambda _: self.deleted_student_dialog.dismiss()
                )
            ]
        )
        self.deleted_student_dialog.open()

    # view gives data to controller
    # controller asks model to make student
    # student is added to table
    def create_new_student(self, *args):
        pass

    def close_enter_path_dialog(self, obj):
        self.file_name_dialog.dismiss()

    def close_student_input_dialog(self, obj):
        self.student_dialog.dismiss()

    def uptade_table_after_deletion(self, new_table, obj):
        self.deleted_student_dialog.dismiss()
        self.data_table.row_data = new_table


def main():
    m = Model()
    c = Controller(m)
    MainApp(c).run()


if __name__ == "__main__":
    main()


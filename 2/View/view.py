from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.dialog import MDDialog

from View.screens_ui import using_navigation


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


class FileAndStudentDialog(Content, AddStudentDialog):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class MainApp(MDApp):
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
                    on_release=function_name
                )
            ]
        )
        self.input_student_dialog.content_cls.ids.input_full_name.hint_text = "enter last name"
        self.input_student_dialog.open()

    def get_students_table_by_path(self, *args):
        self.file_name_dialog.dismiss()
        path = self.file_name_dialog.content_cls.ids.file.text
        message, data = self.controller.download_students(path)
        if message:
            self.open_info_dialog(message)
        self.data_table.row_data = data

    def get_filtered_students(self, *args):
        self.input_student_dialog.dismiss()

        name = self.input_student_dialog.content_cls.ids.input_full_name.text
        group = self.input_student_dialog.content_cls.ids.input_group.text
        sick = self.input_student_dialog.content_cls.ids.input_sick.text
        absent = self.input_student_dialog.content_cls.ids.input_absent.text
        other = self.input_student_dialog.content_cls.ids.input_other.text

        message, filtered_table = self.controller.filters(name, group, sick, absent, other)
        if message:
            self.open_info_dialog(message)
            return None
        return filtered_table

    def show_filtered_students(self, *args):
        data = self.get_filtered_students(*args)
        if data is None:
            return
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

    def show_deleted_students(self, *args):
        data = self.get_filtered_students(*args)
        if data is None:
            return
        self.controller.delete_students(data)
        new_table = self.controller.get_student_table()

        if data:
            text = f"{len(data)} students were deleted"
        else:
            text = "No student was deleted"

        self.deleted_student_dialog = MDDialog(
                title="Deleted Information",
                text=text,
                buttons=[
                    MDRectangleFlatButton(
                        text='Close',
                        theme_text_color='Custom',
                        text_color=self.theme_cls.primary_color,
                        on_release=lambda _: self.update_data_table(new_table),
                    )
                ]
            )
        self.deleted_student_dialog.open()

    def update_data_table(self, *args):
        self.deleted_student_dialog.dismiss()
        new_table = args[-1]
        self.data_table.row_data = new_table

    def open_new_student_dialog(self, function_name):
        self.add_student_dialog = MDDialog(
                    title='Input Student Information',
                    content_cls=AddStudentDialog(),
                    type="custom",
                    buttons=[
                        MDRectangleFlatButton(
                            text='Enter',
                            theme_text_color='Custom',
                            text_color=self.theme_cls.primary_color,
                            on_release=function_name,
                        )
                    ]
                )
        self.add_student_dialog.open()

    def add_new_student_to_table(self, *args):
        self.add_student_dialog.dismiss()

        full_name = self.add_student_dialog.content_cls.ids.input_full_name.text
        group = self.add_student_dialog.content_cls.ids.input_group.text
        sick = self.add_student_dialog.content_cls.ids.input_sick.text
        absent = self.add_student_dialog.content_cls.ids.input_absent.text
        other = self.add_student_dialog.content_cls.ids.input_other.text

        message, new_table = self.controller.add_student_to_table(full_name, group, sick, absent, other)
        if message:
            self.open_info_dialog(message)
        self.data_table.row_data = new_table

    def open_file_and_student_dialog(self):
        self.file_and_student_dialog = MDDialog(
            title='Input File and Student Information',
            content_cls=FileAndStudentDialog(size_hint_y=None,
                                             height=dp(360)),
            type="custom",
            buttons=[
                MDRectangleFlatButton(
                    text='Enter',
                    theme_text_color='Custom',
                    text_color=self.theme_cls.primary_color,
                    on_release=lambda _: self.upload_student_to_file(),
                )
            ]
        )
        self.file_and_student_dialog.open()

    def upload_student_to_file(self, *args):
        self.file_and_student_dialog.dismiss()

        file_name = self.file_and_student_dialog.content_cls.ids.file.text
        name = self.file_and_student_dialog.content_cls.ids.input_full_name.text
        group = self.file_and_student_dialog.content_cls.ids.input_group.text
        sick = self.file_and_student_dialog.content_cls.ids.input_sick.text
        absent = self.file_and_student_dialog.content_cls.ids.input_absent.text
        other = self.file_and_student_dialog.content_cls.ids.input_other.text

        message = self.controller.add_student_to_file(file_name, name, group, sick, absent, other)
        if message:
            self.open_info_dialog(message)

    def open_info_dialog(self, message):
        self.info_dialog = MDDialog(
            title=message,
            buttons=[
                MDRectangleFlatButton(
                    text="Close",
                    on_release=lambda _: self.info_dialog.dismiss()
                )
            ]
        )
        self.info_dialog.open()


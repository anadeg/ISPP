from Model.model import Model


class Controller:
    def __init__(self, model=None):
        self.model = model

    def get_student_table(self):
        return self.model.table_of_students

    def download_students(self, file_name):
        result = []
        message = ''
        try:
            self.model.read_data_from_xml(file_name)
            result = self.model.table_of_students
        except ValueError:
            message = 'File does not exist'
        return message, result

    def add_student_to_table(self, name, group, sick, absent, other):
        message = ''
        to_do = Controller.check_inputs([name, group, sick, absent, other])
        if to_do:
            self.model.add_student_to_table([name, group, sick, absent, other])
        else:
            message = 'You entered wrong field(s)'
        return message, self.get_student_table()

    def filters(self, name, group, sick_interval, absent_interval, other_interval):
        message = ''
        if Controller.are_reasons_int([sick_interval, absent_interval, other_interval], allow_empty=True):
            result = self.model.filters(name, group, sick_interval, absent_interval, other_interval)
        else:
            message = 'You entered wrong field(s)'
            result = []
        return message, result

    def delete_students(self, black_list):
        self.model.delete_students_from_table(black_list)

    def add_student_to_file(self, file_name, name, group, sick, absent, other):
        if Controller.check_inputs([file_name, name, group, sick, absent, other]):
            try:
                message = 'Student was added to file'
                self.model.write_data_in_xml(file_name, [[name, group, sick, absent, other]])
            except FileNotFoundError:
                message = 'New file was created\nStudent was added to this file'
                self.create_new_file(file_name)
                self.model.write_data_in_xml(file_name, [[name, group, sick, absent, other]])
        else:
            message = 'You entered wrong field(s)'
        return message

    def create_new_file(self, file_name):
        path = self.model.get_path_to_file(file_name)
        with open(path, 'w') as new_file:
            new_file.write('<?xml version="1.0" ?>\n<table>\n</table>')

    @staticmethod
    def are_filled(list_of_values):
        for value in list_of_values:
            if not value:
                return False
        return True

    @staticmethod
    def are_reasons_int(list_of_reasons, allow_empty=False):
        for reason in list_of_reasons:
            try:
                if allow_empty:
                    if not reason:
                        continue
                min_value, max_value = Model.get_min_max(reason)
                if min_value is None or max_value is None:
                    raise ValueError
            except ValueError:
                return False
        return True

    @staticmethod
    def check_inputs(values):
        string_properties = values[:-3]
        reasons = values[-3:]
        return Controller.are_filled(string_properties) and Controller.are_reasons_int(reasons)

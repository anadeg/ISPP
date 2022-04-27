# from Model.model import Model
# from View.view import MainApp


class Controller:
    def __init__(self, model=None):
        self.model = model

    def get_student_table(self):
        return self.model.table_of_students

    def download_students(self, file_name):
        result = []
        try:
            self.model.read_data_from_xml(file_name)
            result = self.model.table_of_students
        except ValueError:
            pass
        return result

    def upload_student(self, file_name, new_student):
        try:
            self.model.write_data_in_xml(file_name, [[new_student]])
        except ValueError:
            pass

    def add_student_to_table(self, name, group, sick, absent, other):
        self.model.add_student_to_table([name, group, str(sick), str(absent), str(other)])
        return self.get_student_table()

    def filters(self, name, group, sick_interval, absent_interval, other_interval):
        result = \
            self.model.filters(name, group, sick_interval, absent_interval, other_interval)
        return result

    def delete_students(self, black_list):
        self.model.delete_students_from_table(black_list)

    # def add_student_to_file(self, file_name, name, group, sick, absent, other):
    #     try:
    #         self.model.write_data_in_xml(file_name, [name, group, str(sick), str(absent), str(other)])
    #     except ValueError:
    #         self.create_new_file(file_name)
    #         self.model.write_data_in_xml(file_name, [name, group, str(sick), str(absent), str(other)])
    #
    # def create_new_file(self, file_name):
    #     path = self.model.get_path_to_file(file_name)
    #     with open(path, 'w') as new_file:
    #         new_file.write('<?xml version="1.0" ?>\n<table>\n</table>')

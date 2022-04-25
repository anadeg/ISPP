# from Model.model import Model
# from View.view import MainApp


class Controller:
    # None to run without conflicts
    def __init__(self, model=None):
        self.model = model

    # returns downloaded table of students
    def download_students(self, file_name):
        try:
            self.model.read_data_from_xml(file_name)
        except ValueError:
            return []
        return self.model.table_of_students

    def upload_student(self, file_name, new_student):
        try:
            self.model.write_data_in_xml(file_name, [new_student])
        except ValueError:
            pass

    def add_student_to_table(self, name, group, sick, absent, other):
        pass

    def filters(self, name, group, sick_interval, absent_interval, other_interval):
        result = \
            self.model.filters(self, name, group, sick_interval, absent_interval, other_interval)

    def delete_students(self, name, group, sick_interval, absent_interval, other_interval):
        return len(self.model.filters(self,  name, group, sick_interval, absent_interval, other_interval))

    def filtered_students(self, name, group, sick_interval, absent_interval, other_interval):
        return self.model.filters(self,  name, group, sick_interval, absent_interval, other_interval)

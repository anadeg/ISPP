from Model.model import Model
from View.view import MainApp


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    # returns downloaded table of students
    def download_students(self, path):
        relative_path = "../xmls/"                          # path to folder with files
        path_to_file = ''.join([relative_path, path])
        self.model.table_of_students.clear()                # clear student table to download new file
        try:
            self.model.read_data_from_xml(path_to_file)
        except ValueError:
            return []                                       # no file - no student
        return self.model.table_of_students

    def filters(self, name_filter, group_filter, sick_interval, absent_interval, other_interval):
        reasons = ["sick", "absent", "other"]
        reasons_filters = [sick_interval, absent_interval, other_interval]
        filtered_table = self.model.table_of_students
        if not name_filter:
            filtered_table = self.model.filter_by_surname(filtered_table, name_filter)
        if not group_filter:
            filtered_table = self.model.filter_by_group(filtered_table, group_filter)
        for i, given_filter in enumerate(reasons_filters):
            if not given_filter:
                min_value, max_value = Controller.get_min_max(reasons_filters[i])
                filtered_table = self.model.filter_by_reason(filtered_table, reasons[i], min_value, max_value)

        return filtered_table

    # convert string "1 <= ... <= 10"
    # returns "1", "10"
    @staticmethod
    def get_min_max(reason_string):
        reason_string = reason_string.replace(" ", "")
        cleared_string = reason_string.split("<=")
        min_value, max_value = cleared_string[0], cleared_string[-1]
        return min_value, max_value

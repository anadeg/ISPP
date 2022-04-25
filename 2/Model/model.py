import bisect
import xml.sax
import os


from xmls.sax_reader import StudentHandler
from xmls.dom_writer import StudentWriter
from Model.student import Student
# from Controller.controller import Controller


class Model:
    def __init__(self, table_of_students):
        self.table_of_students = []
        for student in table_of_students:
            bisect.insort(self.table_of_students, student)

    @staticmethod
    def get_path_to_file(file_name):
        relative_path = "../xmls/"                  # path to folder with files
        return ''.join([relative_path, file_name])

    def read_data_from_xml(self, file_name):
        path_to_file = Model.get_path_to_file(file_name)
        self.table_of_students.clear()

        handler = StudentHandler()
        parser = xml.sax.make_parser()
        parser.setContentHandler(handler)
        parser.parse(path_to_file)

        data = {}
        for student_data in handler.student_table:
            while student_data:
                data.update(student_data)
                break
            else:
                if len(data) == 5:
                    self.add_student_to_table(data)
                    data = {}

    @staticmethod
    def write_data_in_xml(file_name, table_with_new_student):
        path_to_file = Model.get_path_to_file(file_name)
        writer = StudentWriter(path_to_file)
        for student in table_with_new_student:
            writer.create_student(student.__dict__)
        writer.add_students_to_xml()

    def add_student_to_table(self, student_data):
        s = Student(**student_data)
        bisect.insort(self.table_of_students, s)

    @staticmethod
    def filter_by_surname(table_of_students, surname):
        surnames_list = [s.name[1] for s in table_of_students]

        start_index = bisect.bisect_left(surnames_list, surname)
        last_index = bisect.bisect_right(surnames_list, surname)

        return table_of_students[start_index:last_index]

    @staticmethod
    def filter_by_group(table_of_students, group):
        student_from_group = []

        for student in table_of_students:
            if student.group == group:
                student_from_group.append(student)

        return student_from_group

    # no reason to convert str to int
    # python already compares it properly
    @staticmethod
    def filter_by_reason(table_of_students, reason, min_amount, max_amount):
        students_properties_dict = [student.__dict__ for student in table_of_students]
        result = []
        for i, student_dict in enumerate(students_properties_dict):
            if min_amount <= student_dict[reason] <= max_amount:
                result.append(table_of_students[i])

        return result

    def filters(self, name_filter, group_filter, sick_interval, absent_interval, other_interval):
        reasons = ["sick", "absent", "other"]
        reasons_filters = [sick_interval, absent_interval, other_interval]
        filtered_table = self.table_of_students
        if not name_filter:
            filtered_table = self.filter_by_surname(filtered_table, name_filter)
        if not group_filter:
            filtered_table = self.filter_by_group(filtered_table, group_filter)
        for i, given_filter in enumerate(reasons_filters):
            if not given_filter:
                min_value, max_value = Model.get_min_max(reasons_filters[i])
                filtered_table = self.filter_by_reason(filtered_table, reasons[i], min_value, max_value)
        return filtered_table

    @staticmethod
    def get_min_max(reason_string):
        reason_string = reason_string.replace(" ", "")
        cleared_string = reason_string.split("<=")
        min_value, max_value = cleared_string[0], cleared_string[-1]
        return min_value, max_value

    def delete_students_from_table(self, black_list):
        for student in black_list:
            try:
                self.table_of_students.remove(student)
            except Exception:
                pass


def main():
    s = Student("john", "24", "0", "0", "0")
    m = Model([])
    relative_path = "../xmls/"
    path_to_file = ''.join([relative_path, "data0.xml"])
    try:
        m.write_data_in_xml(path_to_file, [s])
    except ValueError:
        pass
    try:
        m.table_of_students.clear()
        m.read_data_from_xml(path_to_file)
    except ValueError:
        pass
    print(*m.table_of_students)


if __name__ == "__main__":
    main()

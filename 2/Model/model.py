import bisect
import xml.sax
import os


from xmls.sax_reader import StudentHandler
from xmls.dom_writer import StudentWriter
from View.generate_table import generate_table


class Model:
    def __init__(self, table_of_students=[]):
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
        characteristics = ["name", "group", "sick", "absent", "other"]
        path_to_file = Model.get_path_to_file(file_name)
        writer = StudentWriter(path_to_file)
        for student in table_with_new_student:
            student_dict = {characteristics[i]: student[i] for i in range(len(student))}
            writer.create_student(student_dict)
        writer.add_students_to_xml()

    def add_student_to_table(self, student_data):
        bisect.insort(self.table_of_students, student_data)

    @staticmethod
    def filter_by_surname(table_of_students, surname):
        # surnames_list = [s[0].split()[-1] for s in table_of_students]
        result = []
        # start_index = bisect.bisect_left(surnames_list, surname)
        # last_index = bisect.bisect_right(surnames_list, surname)
        for student in table_of_students:
            if student[0].split()[-1] == surname:
                result.append(student)

        return result

    @staticmethod
    def filter_by_group(table_of_students, group):
        student_from_group = []

        for student in table_of_students:
            if student[1] == group:
                student_from_group.append(student)

        return student_from_group

    # no reason to convert str to int
    # python already compares it properly
    @staticmethod
    def filter_by_reason(table_of_students, reason, min_amount, max_amount):
        # students_properties_dict = [student.__dict__ for student in table_of_students]
        reasons = ["sick", "absent", "other"]
        reason_index = reasons.index(reason) + 2    # because of name and group
        result = []
        for student in table_of_students:
            if min_amount <= student[reason_index] <= max_amount:
                result.append(student)

        return result

    def filters(self, name_filter, group_filter, sick_interval, absent_interval, other_interval):
        reasons = ["sick", "absent", "other"]
        reasons_filters = [sick_interval, absent_interval, other_interval]
        filtered_table = self.table_of_students
        if name_filter:
            filtered_table = Model.filter_by_surname(filtered_table, name_filter)
        if group_filter:
            filtered_table = Model.filter_by_group(filtered_table, group_filter)
        for i, given_filter in enumerate(reasons_filters):
            if given_filter:
                min_value, max_value = Model.get_min_max(reasons_filters[i])
                filtered_table = Model.filter_by_reason(filtered_table, reasons[i], min_value, max_value)
        return filtered_table

    @staticmethod
    def get_min_max(reason_string):
        reason_string = reason_string.replace(" ", "")
        cleared_string = reason_string.split("<=")
        min_value, max_value = cleared_string[0], cleared_string[-1]
        return min_value, max_value

    def delete_students_from_table(self, black_list):
        deleted_indexes = []
        try:
            for student in black_list:
                index = self.table_of_students.index(student)
                deleted_indexes.append(index)
            for index in deleted_indexes:
                self.table_of_students.pop(index)
        except Exception:
            pass
        return deleted_indexes

def main():
    m = Model([])
    relative_path = "../xmls/"
    path_to_file = ''.join([relative_path, "data2.xml"])
    # table = generate_table(50)
    # m.write_data_in_xml(path_to_file, table)
    # try:
    #     m.write_data_in_xml(path_to_file, [s])
    # except ValueError:
    #     pass
    try:
        # m.table_of_students.clear()
        m.read_data_from_xml(path_to_file)
    except ValueError:
        pass
    print(*m.table_of_students)


if __name__ == "__main__":
    main()

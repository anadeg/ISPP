import bisect
import xml.sax
import os


from xmls.sax_reader import StudentHandler
from xmls.dom_writer import StudentWriter
from student import Student




class Model:
    def __init__(self, table_of_students):
        self.table_of_students = []
        self.deleted_count = 0
        for student in table_of_students:
            bisect.insort(self.table_of_students, student)

    def read_data_from_xml(self, file_name):
        handler = StudentHandler()
        parser = xml.sax.make_parser()
        parser.setContentHandler(handler)
        parser.parse(file_name)

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
    def write_data_in_xml(file_name, table_with_tables):
        writer = StudentWriter(file_name)
        for student in table_with_tables:
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

    @staticmethod
    def filter_by_reason(table_of_students, reason, min_amount, max_amount):
        students_properties_dict = [student.__dict__ for student in table_of_students]
        result = []
        for i, student_dict in enumerate(students_properties_dict):
            if min_amount <= student_dict[reason] <= max_amount:
                result.append(table_of_students[i])

        return result

    def delete_students_from_table(self, black_list):
        for student in black_list:
            try:
                self.table_of_students.remove(student)
                self.deleted_count += 1
            except Exception:
                pass


def main():
    s = Student("john", "24", "0", "0", "0")
    m = Model([])
    m.write_data_in_xml("../xmls/data0.xml", [s])
    relative_path = "../xmls/"
    m.read_data_from_xml("".join([relative_path, "data0.xml"]))
    print(*m.table_of_students)


if __name__ == "__main__":
    main()

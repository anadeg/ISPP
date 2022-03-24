import bisect
import xml.sax

from xmls.sax_reader import StudentHandler
from xmls.dom_writer import StudentWriter
from student import Student


class Model:
    def __init__(self, table_of_students):
        self.table_of_students = []
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
                if data:
                    self.add_student_to_table(data)
                    data = {}

    def write_data_in_xml(self, file_name):
        writer = StudentWriter(file_name)
        for student in self.table_of_students:
            writer.create_student(student.__dict__)
        writer.add_students_to_xml()

    def add_student_to_table(self, student_data):
        s = Student(**student_data)
        bisect.insort(self.table_of_students, s)

    def filter_by_surname(self, surname):
        surnames_list = [s.name[1] for s in self.table_of_students]

        start_index = bisect.bisect_left(surnames_list, surname)
        last_index = bisect.bisect_right(surnames_list, surname)

        return self.table_of_students[start_index:last_index]

    def filter_by_group(self, group):
        student_from_group = []

        for student in self.table_of_students:
            if student.group == group:
                student_from_group.append(student)

        return student_from_group


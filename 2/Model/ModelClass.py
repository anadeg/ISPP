import bisect
import xml.sax

from xmls.sax_reader import StudentHandler
from xmls.dom_writer import StudentWriter
from Student import Student


class Model:
    def __init__(self, table_of_students):
        self.table_of_students = table_of_students

    def read_data_from_xml(self, file_name):
        handler = StudentHandler()
        parser = xml.sax.make_parser()
        parser.setContentHandler(handler)
        parser.parse("xmls/" + file_name)

        for student_data in handler.student_table:
            self.add_student_to_table(student_data)

    def write_data_in_xml(self, file_name):
        writer = StudentWriter(file_name)
        for student in self.table_of_students:
            writer.create_student(student.__dict__)
            writer.add_students_to_xml()

    def add_student_to_table(self, student_data):
        s = Student(**student_data)
        bisect.insort(self.table_of_students, s)





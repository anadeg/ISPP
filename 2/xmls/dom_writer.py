import xml.dom.minidom


class StudentWriter:
    def __init__(self, filename):
        self.file_name = filename
        self.domtree = xml.dom.minidom.parse(filename)
        self.group = self.domtree.documentElement

    def create_student(self, characteristics):
        student = self.domtree.createElement("student")

        for characteristic in characteristics:
            temporary_value = self.domtree.createElement(characteristic)
            temporary_value.appendChild(self.domtree.createTextNode(characteristics[characteristic].strip()))

            student.appendChild(temporary_value)

        self.group.appendChild(student)

    def add_students_to_xml(self):
        self.domtree.writexml(open(self.file_name, "w"), indent=" ", addindent=" ", newl="\n")
        self.domtree.unlink()

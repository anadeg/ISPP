import xml.sax


class StudentHandler(xml.sax.ContentHandler):
    def __init__(self):
        super().__init__()
        self.student_table = []
        self.student_data = {}

    def startElement(self, name, attrs):
        self.current = name
        if name == "student":
            pass

    def characters(self, content):
        if self.current == "name":
            self.name = content
        elif self.current == "group":
            self.group = content
        elif self.current == "sick":
            self.sick = content
        elif self.current == "absent":
            self.absence = content
        elif self.current == "other":
            self.other = content

    def endElement(self, name):
        if self.current == "name":
            self.student_data["name"] = self.name
        elif self.current == "group":
            self.student_data["group"] = self.group
        elif self.current == "sick":
            self.student_data["sick"] = self.sick
        elif self.current == "absent":
            self.student_data["absent"] = self.absence
        elif self.current == "other":
            self.student_data["other"] = self.other

        self.student_table.append(self.student_data)
        self.student_data = {}

        self.current = ""


def main():
    handler = StudentHandler()
    parser = xml.sax.make_parser()
    parser.setContentHandler(handler)
    parser.parse("data0.xml")
    for student_data in handler.student_table:
        print(student_data)


if __name__ == "__main__":
    main()
import xml.sax


class StudentHandler(xml.sax.ContentHandler):
    def __init__(self):
        super().__init__()
        self.student_table = []
        self.student_data = {}

    def startElement(self, name):
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
        elif self.current == "absence":
            self.absence = content
        elif self.current == "other":
            self.other = content

    def endElement(self):
        if self.current == "name":
            self.student_data["name"] = self.name
        elif self.current == "group":
            self.student_data["group"] = self.group
        elif self.current == "sick":
            self.student_data["sick"] = self.sick
        elif self.current == "absence":
            self.student_data["absence"] = self.absence
        elif self.current == "other":
            self.student_data["other"] = self.other

        self.student_table.append(self.student_data)
        self.student_data = {}

        self.current = ""

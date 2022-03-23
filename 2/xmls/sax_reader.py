import xml.sax


class StudentHandler(xml.sax.ContentHandler):
    def startElement(self, name, attrs):
        self.current = name
        # if name == "student":
        #     print(f"======== STUDENT {attrs['id']} ========")

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

    def endElement(self, name):
        if self.current == "name":
            print(f"-- name: {self.name} --")
        elif self.current == "group":
            print(f"-- group: {self.group} --")
        elif self.current == "sick":
            print(f"-- sick time: {self.sick} --")
        elif self.current == "absence":
            print(f"-- absence time: {self.absence} --")
        elif self.current == "other":
            print(f"-- other time: {self.other} --")

        self.current = ""


handler = StudentHandler()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
parser.parse('data0.xml')

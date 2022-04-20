screens = """


ScreenManager:
    InputPathScreen:
    ShowStudentsScreen:
    
<ShowStudentsScreen>:
    name: 'table'
    MDRectangleFlatButton:
        text: 'go to me'
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        
<InputPathScreen>:
    name: 'input path'
    MDTextField:
        hint_text: "enter file name"
        helper_text: "like data.txt, data0.xml and so on"
        helper_text_mode: "on_focus"
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        size_hint_x: 0.5
        icon_right: "file-document-multiple"
    MDRectangleFlatButton:
        text: "go to table"
        pos_hint: {"center_x": 0.5, "center_y": 0.4}
        on_release: root.manager.current = 'table'
"""
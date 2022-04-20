# ScreenManager:
# main ---  show (download) student screen --------------|
#               window with field (path)                 |
#               table                                    |
#                                                   lists navigation
#           delete student screen                        |
#           add student screen                           |
#           filter student screen -----------------------
#

text_ui = """
MDScreen:
    MDNavigationLayout:
        ScreenManager:
            MDScreen:
                MDBoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'demo app'
                        left_action_items: [["menu", lambda x: drawer.set_state("open")]]
                    Widget:
                    
        MDNavigationDrawer:
            id: drawer
            BoxLayout:
                orientation: 'vertical'
                spacing: '8dp'
                padding: '8dp'
                MDLabel:
                    size_hint_y: 0.1
                    text: "Choose option"
                    
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: "item 1"
                            IconLeftWidget:
                                icon: 'language-python'
                        OneLineIconListItem:
                            text: "upload"
                            IconLeftWidget:
                                icon: 'file-upload'
                        OneLineListItem:
                            text: "item 1"
                
    
"""

enter_path = """
MDTextField:
    hint_text: "enter file name"
    helper_text: "like data.txt, data0.xml and so on"
    helper_text_mode: "on_focus"
    pos_hint: {"center_x": 0.5, "center_y": 0.5}
    size_hint_x: 0.5
    icon_right: "file-document-multiple"
"""

enter_path_button = """
MDScreen:
    MDRectangleFlatButton:
        text: "show"
        pos_hint: {"center_x": 0.5, "center_y": 0.4}
        on_release: app.show_path
"""

path_dialog = """
MDDialog:
    title: "path input"
    text: app.input_path_text
    MDFlatButton:
        text: "close"
        on_release: app.close_dialog
    MDFlatButton:
        text: "more"
"""
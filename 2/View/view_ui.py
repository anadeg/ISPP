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
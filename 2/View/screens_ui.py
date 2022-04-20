screens = """
MDNavigationLayout:
    MDNavigationDrawer:
        NavigationDrawerIconButton:
            text: "input path"
            on_release: screen_manager.current = 'input_screen'
        NavigationDrawerIconButton:
            text: "show table"
            on_release: screen_manager.current = 'table_screen'
                
    ScreenManager:
        id: "screen_manager"
        InputPathScreen:
        ShowStudentsScreen:
        
<ShowStudentsScreen>:
    name: 'table_screen'
    MDRectangleFlatButton:
        text: 'go to me'
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
            
<InputPathScreen>:
    name: 'input_screen'
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


screens2 = """
<ContentNavigationDrawer>:
    ScrollView:
        MDList:
            OneLineIconListItem:
                text: 'enter path'
                on_press:
                    root.drawer.set_state("close")
                    root.screen_manager.current = 'input_screen'
                IconLeftWidget:
                    icon: 'file-multiple'
            OneLineIconListItem:
                text: 'table'
                on_press:
                    root.drawer.set_state("close")
                    root.screen_manager.current = 'table_screen'
                IconLeftWidget:
                    icon: 'file-table'
                    
Screen:
    MDToolbar:
        id: toolbar
        pos_hint: {"top": 1}
        elevation: 10
        title: "menu"
        left_action_items: [["menu", lambda x: drawer.set_state("open")]]
        
    MDNavigationLayout:
        x: toolbar.height
        ScreenManager:
            id: screen_manager
            InputPathScreen:
            ShowStudentsScreen:
            
    MDNavigationDrawer:
        id: drawer
        ContentNavigationDrawer:
            screen_manager: screen_manager
            drawer: drawer
            
            

<ShowStudentsScreen>:
    name: 'table_screen'
    MDRectangleFlatButton:
        text: 'go to me'
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
            
<InputPathScreen>:
    name: 'input_screen'
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
        on_release: root.manager.current = 'table_screen'
"""

content_of_entering_path = """
<Content>:
    orientation: 'vertical'
    spacing: '8dp'
    size_hint_y :None
    height: '40dp'
    
    MDTextField:
        id: file
        hint_text: 'enter file name'
        helper_text: 'file must be in folder "xmls"'
        helper_text_mode: 'on_focus'
"""

using_navigation = """
Screen:
    MDToolbar:
        id: toolbar
        pos_hint: {"top": 1}
        elevation: 10
        title: "menu"
        left_action_items: [["menu", lambda x: drawer.set_state("open")]]
        
        MDNavigationLayout:
            x: toolbar.height
        
    MDNavigationDrawer:
        id: drawer
        ContentNavigationDrawer:
            drawer: drawer

<ContentNavigationDrawer>:
    ScrollView:
        MDList:
            OneLineIconListItem:
                text: "enter path"
                on_press: 
                    root.drawer.set_state("close")
                    app.open_file_name_dialog()
                IconLeftWidget:
                    icon: 'file-multiple'
                    
"""
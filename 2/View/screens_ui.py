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
            OneLineIconListItem:
                text: "filter student"
                on_press: 
                    root.drawer.set_state("close")
                    app.open_input_student_dialog(app.get_filtered_students)
                IconLeftWidget:
                    icon: 'filter'
                    
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
        
        
<TextField@MDTextField>:
    size_hint: 0.5, 0.1
    input_type: "text"
    
    
<StudentDataDialog>:
    id: student_data_dialog
    name: 'student_data_dialog'
    
    orientation: "vertical"
    spacing: "12dp"
    size_hint_y: None
    height: "300dp"
    
    full_name: input_full_name
    group: input_group
    sick: input_sick
    absent: input_absent
    other: input_other


    TextField:
        id: input_full_name
        hint_text: "enter full name"

    TextField:
        id: input_group
        hint_text: "enter group"

    TextField:
        id: input_sick
        hint_text: "enter sick"
        helper_text: "enter interval like 10 <= n <= 34"
        helper_text_mode: 'on_focus'

    TextField:
        id: input_absent
        hint_text: "enter absent"
        helper_text: "enter interval like 10 <= n <= 34"
        helper_text_mode: 'on_focus'

    TextField:
        id: input_other
        hint_text: "enter other"
        helper_text: "enter interval like 10 <= n <= 34"
        helper_text_mode: 'on_focus'
        
                    
"""
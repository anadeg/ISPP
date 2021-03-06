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
                text: "Add New Student to Table"
                on_press: 
                    root.drawer.set_state("close")
                    app.open_new_student_dialog(app.add_new_student_to_table)
                IconLeftWidget:
                    icon: 'account-plus-outline'
            
            OneLineIconListItem:
                text: "Download Students from File"
                on_press: 
                    root.drawer.set_state("close")
                    app.open_file_name_dialog(app.get_students_table_by_path)
                IconLeftWidget:
                    icon: 'download-outline'
                    
            OneLineIconListItem:
                text: "Filter Students from Table"
                on_press: 
                    root.drawer.set_state("close")
                    app.open_input_student_dialog(app.show_filtered_students)
                IconLeftWidget:
                    icon: 'filter-outline'
                    
            OneLineIconListItem:
                text: "Delete Students from Table"
                on_press: 
                    root.drawer.set_state("close")
                    app.open_input_student_dialog(app.show_deleted_students)
                IconLeftWidget:
                    icon: 'delete-outline'
                    
            OneLineIconListItem:
                text: "Upload Student to File"
                on_press: 
                    root.drawer.set_state("close")
                    app.open_file_and_student_dialog()
                IconLeftWidget:
                    icon: 'upload-outline'

                    
<Content>:
    orientation: 'vertical'
    spacing: '8dp'
    size_hint_y :None
    height: '30dp'
    
    TextField:
        id: file
        hint_text: 'enter file name'
        helper_text: 'file must be in folder "xmls"'
        helper_text_mode: 'on_focus'
        
        
<TextField@MDTextField>:
    size_hint: 0.9, 0.07
    input_type: "text"
    
<StudentDataDialog>:
    id: student_data_dialog
    name: 'student_data_dialog'
    
    orientation: "vertical"
    spacing: "8dp"
    size_hint_y: None
    height: "280dp"
    
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


<IntField@MDTextField>:
    size_hint: 0.9, 0.1
    input_type: "text"
    
<AddStudentDialog>:
    id: add_student_dialog
    name: 'add_student_dialog'
    
    orientation: "vertical"
    spacing: "8dp"
    size_hint_y: None
    height: "280dp"
    
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
        helper_text: "enter integer like 10"
        helper_text_mode: 'on_focus'

    TextField:
        id: input_absent
        hint_text: "enter absent"
        helper_text: "enter integer like 10"
        helper_text_mode: 'on_focus'

    TextField:
        id: input_other
        hint_text: "enter other"
        helper_text: "enter integer like 10"
        helper_text_mode: 'on_focus'
        
"""
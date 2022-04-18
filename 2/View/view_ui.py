# KV = '''
#
# #:import md_icons kivymd.icon_definitions.md_icons
# #:import fonts kivymd.font_definitions.fonts
#
# # Menu item in the DrawerList list.
# <ItemDrawer>:
#     theme_text_color: "Custom"
#     on_release: self.parent.set_color_item(self)
#
#     IconLeftWidget:
#         id: icon
#         icon: root.icon
#         theme_text_color: "Custom"
#         text_color: root.text_color
#
#
# <ContentNavigationDrawer>:
#     orientation: "vertical"
#     padding: "8dp"
#     spacing: "8dp"
#
#     AnchorLayout:
#         anchor_x: "left"
#         size_hint_y: None
#         height: avatar.height
#
#         Image:
#             id: avatar
#             size_hint: None, None
#             size: "56dp", "56dp"
#             source: "data/logo/kivy-icon-256.png"
#
#     MDLabel:
#         text: "Client base app"
#         font_style: "Button"
#         size_hint_y: None
#         height: self.texture_size[1]
#
#     MDLabel:
#         text: "author Nero"
#         font_style: "Caption"
#         size_hint_y: None
#         height: self.texture_size[1]
#
#     ScrollView:
#
#         MDList:
#             id: md_list
#             OneLineIconListItem:
#                 text: "Upload data base"
#                 on_release: app.upload()
#                 IconLeftWidget:
#                     icon: "upload"
#
#             OneLineIconListItem:
#                 text: "Save data base"
#                 on_release: app.save()
#                 IconLeftWidget:
#                     icon: "content-save"
#
#             OneLineIconListItem:
#                 text: "Dark/Light"
#                 on_release: app.color_theme()
#                 IconLeftWidget:
#                     icon: "shield-sun"
#
#
#
#
# Screen:
#
#     MDNavigationLayout:
#
#         ScreenManager:
#
#             Screen:
#
#                 BoxLayout:
#                     orientation: 'vertical'
#
#                     MDToolbar:
#                         title: "Client base"
#                         elevation: 10
#                         left_action_items: [['menu', lambda x: nav_drawer.set_state("open")]]
#                         md_bg_color: 0,0,0,1
#
#                     MDTabs:
#                         id: tabs
#                         height: "48dp"
#                         tab_indicator_anim: False
#                         background_color: 0.1,0.1,0.1,1
#
#                         Tab:
#                             id: tab1
#                             name: 'tab 1'
#                             text: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['table-large']}[/size][/font] Table"
#                             ScrollView:
#                                 MDList:
#                                     id: widget_label
#
#
#                         Tab:
#                             id: tab2
#                             name: 'tab 2'
#                             text: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['clock-time-eight-outline']}[/size][/font] View logs"
#                             ScrollView:
#                                 MDList:
#                                     id: widget_label_view
#
#
#                         Tab:
#                             id: tab3
#                             name: "tab 3"
#                             text: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['account-arrow-up']}[/size][/font] Create user"
#                             BoxLayout:
#                                 orientation: 'vertical'
#                                 padding: "10dp"
#
#                                 BoxLayout:
#                                     orientation: 'horizontal'
#
#                                     MDIconButton:
#                                         icon: "account"
#
#                                     MDTextField:
#                                         id: name
#                                         hint_text: 'Name'
#
#                                 BoxLayout:
#                                     orientation: 'horizontal'
#
#                                     MDIconButton:
#                                         icon: "numeric"
#
#                                     MDTextField:
#                                         id: account_number
#                                         hint_text: 'Account number'
#
#
#                                 BoxLayout:
#                                     orientation: 'horizontal'
#
#                                     MDIconButton:
#                                         icon: "badge-account-horizontal-outline"
#
#                                     MDTextField:
#                                         id: address
#                                         hint_text: 'Address'
#
#                                 BoxLayout:
#                                     orientation: 'horizontal'
#
#                                     MDIconButton:
#                                         icon: "cellphone"
#
#                                     MDTextField:
#                                         id: mobile_phone
#                                         hint_text: 'Mobile phone'
#
#                                 BoxLayout:
#                                     orientation: 'horizontal'
#
#                                     MDIconButton:
#                                         icon: "phone"
#
#                                     MDTextField:
#                                         id: home_phone
#                                         hint_text: 'Home phone'
#
#                                 BoxLayout:
#                                     MDRectangleFlatButton:
#                                         text: "Confirm new user and save info"
#                                         theme_text_color: "Custom"
#                                         text_color: 1, 0, 1, 1
#                                         line_color: 0, 0, 1, 1
#                                         on_release: app.update_user_base()
#
#                                     MDRectangleFlatButton:
#                                         text: "Back and clear all info fields"
#                                         theme_text_color: "Custom"
#                                         text_color: 1, 0, 1, 1
#                                         line_color: 0, 0, 1, 1
#                                         on_release: app.clear_fields()
#
#                         Tab:
#                             id: tab4
#                             name: "tab 4"
#                             text: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['account-search']}[/size][/font] Search user"
#                             BoxLayout:
#                                 orientation: 'vertical'
#                                 padding: "10dp"
#
#                                 BoxLayout:
#                                     orientation: 'horizontal'
#
#                                     MDIconButton:
#                                         icon: "account"
#
#                                     MDTextField:
#                                         id: name_for_search
#                                         hint_text: 'Name'
#
#                                 BoxLayout:
#                                     orientation: 'horizontal'
#
#                                     MDIconButton:
#                                         icon: "numeric"
#
#                                     MDTextField:
#                                         id: account_number_for_search
#                                         hint_text: 'Account number'
#
#
#                                 BoxLayout:
#                                     orientation: 'horizontal'
#
#                                     MDIconButton:
#                                         icon: "badge-account-horizontal-outline"
#
#                                     MDTextField:
#                                         id: address_for_search
#                                         hint_text: 'Address'
#
#                                 BoxLayout:
#                                     orientation: 'horizontal'
#
#                                     MDIconButton:
#                                         icon: "cellphone"
#
#                                     MDTextField:
#                                         id: mobile_phone_for_search
#                                         hint_text: 'Mobile phone'
#
#                                 BoxLayout:
#                                     orientation: 'horizontal'
#
#                                     MDIconButton:
#                                         icon: "phone"
#
#                                     MDTextField:
#                                         id: home_phone_for_search
#                                         hint_text: 'Home phone'
#
#                                 BoxLayout:
#                                     MDRectangleFlatButton:
#                                         text: "Search user in base"
#                                         theme_text_color: "Custom"
#                                         text_color: 1, 0, 1, 1
#                                         line_color: 0, 0, 1, 1
#                                         on_release: app.search_user_info()
#
#                                     MDRectangleFlatButton:
#                                         text: "Back and clear all info fields"
#                                         theme_text_color: "Custom"
#                                         text_color: 1, 0, 1, 1
#                                         line_color: 0, 0, 1, 1
#                                         on_release: app.clear_fields()
#
#                         Tab:
#                             id: tab5
#                             name: "tab 5"
#                             text: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['delete']}[/size][/font] Delete user"
#                             BoxLayout:
#                                 orientation: 'vertical'
#                                 padding: "10dp"
#
#                                 BoxLayout:
#                                     orientation: 'horizontal'
#
#                                     MDIconButton:
#                                         icon: "account"
#
#                                     MDTextField:
#                                         id: name_for_delete
#                                         hint_text: 'Name'
#
#                                 BoxLayout:
#                                     orientation: 'horizontal'
#
#                                     MDIconButton:
#                                         icon: "numeric"
#
#                                     MDTextField:
#                                         id: account_number_for_delete
#                                         hint_text: 'Account number'
#
#
#                                 BoxLayout:
#                                     orientation: 'horizontal'
#
#                                     MDIconButton:
#                                         icon: "badge-account-horizontal-outline"
#
#                                     MDTextField:
#                                         id: address_for_delete
#                                         hint_text: 'Address'
#
#                                 BoxLayout:
#                                     orientation: 'horizontal'
#
#                                     MDIconButton:
#                                         icon: "cellphone"
#
#                                     MDTextField:
#                                         id: mobile_phone_for_delete
#                                         hint_text: 'Mobile phone'
#
#                                 BoxLayout:
#                                     orientation: 'horizontal'
#
#                                     MDIconButton:
#                                         icon: "phone"
#
#                                     MDTextField:
#                                         id: home_phone_for_delete
#                                         hint_text: 'Home phone'
#
#                                 BoxLayout:
#                                     MDRectangleFlatButton:
#                                         text: "Find and delete user info"
#                                         theme_text_color: "Custom"
#                                         text_color: 1, 0, 1, 1
#                                         line_color: 0, 0, 1, 1
#                                         on_release: app.delete_user_info()
#
#                                     MDRectangleFlatButton:
#                                         text: "Back and clear all info fields"
#                                         theme_text_color: "Custom"
#                                         text_color: 1, 0, 1, 1
#                                         line_color: 0, 0, 1, 1
#                                         on_release: app.clear_fields()
#
#         MDNavigationDrawer:
#             id: nav_drawer
#
#             ContentNavigationDrawer:
#                 id: content_drawer
# '''
text_ui = """
Screen:
    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'demo app'
                        left_action_items: [["menu", lambda x: drawer.toggle_drawer()]]
                    MDLabel:
                        text: 'fuck it'
                        halign: 'center'
        MDNavigationDrawer:
            id: drawer
                
    
"""
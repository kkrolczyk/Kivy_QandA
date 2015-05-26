"""

#    SOME KIVY ITEMS TO REMEMBER
#
# 1. Any class defined in *.kv file must have 'forward declaration' in *.py
#
# 2. Two main ideas for accessing kv <=> py:
#    a) either via {Object|String|...}Property in both kv/py
#    b) or via root.ids.id_object1_name.id_object2_name.property
#
# 3. Prevent having item/button/object fill whole Layout, plus Popup usage demo
#
# class ContainerForButtons(GridLayout):
#     def __init__(self, **kwargs):
#         super(ContainerForButtons, self).__init__(**kwargs)
#         # prevent dynamically added buttons scaling to fill whole parent
#         self.bind(minimum_height=self.setter("height"))
#         # generally, it appears that only widgets' build() is automatically
#         # triggered, so here we do it by ourselves
#         self.build()
#     def build(self):
#         self.clear_widgets()  # in case we'd like to re enumerate buttons
#         self.add_some_buttons()
#     def add_some_buttons(self):  # dynamically create CustomButtons
#         buttons_descriptions = [ chr(i) for i in range(65, 75) ]
#         for item in buttons_descriptions:
#             # CustomButtonClass 'template' is defined in KV file, for example:
#             #     <CustomButton@Button>:
#             #        description_a: ''
#             #        description_b: ''
#             #        text: root.description_a + "\n" + root.description_b
#             #        halign:'center'
#             #        size_hint:(1, 0.1)
#             # no 'forward declaration' is needed
#             # > from kivy.factory import Factory
#             btn = Factory.CustomButtonClass()
#             btn.description_a = item
#             btn.description_b = "some other thing"
#             btn.bind(on_press=self.execute_action_using_button_item)
#         if not buttons_descriptions:
#             err = "Inform user that there are no descriptions."
#             self.add_widget(Label(text=err))
#         def execute_action_using_button_item(self):
#             # We might also use popup above, for example like this:
#             # > from kivy.uix.popup import Popup
#             # > from kivy.uix.label import Label
#             popup = Popup(title="Button callback",
#                           content=Label(text="".join(map(repr, args))))
#             popup.open()
#             # > from kivy.clock import Clock
#             Clock.schedule_once(popup.dismiss, 1)  # close after a second
#
# 4. If Label/Button wanted that does not get overflown
#     but scrolls/wraps it's contents
#
# # in Python code...
#
# from kivy.uix.scrollview import ScrollView
# from kivy.properties import StringProperty
# class LabelThatScrolls(ScrollView):
#   text = StringProperty('')
#
# # in Kivy's KV
# <LabelThatScrolls>:
#     Label:
#         size_hint_y: None
#         height: self.texture_size[1]
#         text_size: self.width, None
#         text: root.text
# <ButtonThatScales>:
#     Button:
#         width: self.texture_size[0] # wraps too long strings, or adjusts btn
#
#
# 5. Using screens and Screen manager, and handling keys that Window receives
#
# from kivy.uix.screenmanager import ScreenManager, Screen
# class MyExample(App):
#     screen_mgr = None
#     def build(self):
#         # bind key event to function callback
#         Window.bind(on_keyboard=self.check_what_key_was_pressed)
#
#         self.screen_mgr = ScreenManager()
#
#         # 'First' is using Screen created from code -
#         # we need to add widgets to it manually
#
#         first = Screen(name='First')
#         self.screen_mgr.add_widget(first)
#         first.add_widget(Button(text="click me", bind=app.swap_screen))
#
#         # We need to make sure that OtherNamedScreen exists in KV, and
#         # it's 'forward declaration' is also present in Python
#         # ie: class OtherNamedScreen(Screen): pass
#         self.screen_mgr.add_widget(OtherNamedScreen(name='Second'))
#
#         return self.screen_mgr
#
#     def swap_screen(self):
#        app.screen_mgr.current = app.screen_mgr.next()
#
#     @staticmethod
#     def check_what_key_was_pressed(window, key_no, *some_other_args):
#         if key_no == 27:  # Android's BACK button
#             app.swap_screen()
#         # elif key in (282, 319):  # SETTINGS button
#         return True  # inform system that key has been handled
#
# 6. Detecting Android window size or orientation - no idea...
#
#       import jnius
#       app.config = jnius.autoclass('android.content.res.Configuration')
#       app.config.screenHeightDp
#       app.config.screenWidthDp
#       app.config.orientation
#
# would be quite useless - since Kivy uses own window manager
#
# 7. Using KV builder class from Python code
#
# from kivy.lang import Builder
# Builder.load_string('''
# <MyListView>:
#    ListView:
#        item_strings: [str(index) for index in range(100)]
# ''')
#
#
# 8. Remember about textwrap.dedent :)
#
#   EXAMPLE FOR MOST OF ABOVE minus stripped comments (TODO: add missing later)

"""

import textwrap
from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.factory import Factory
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen

class OtherNamedScreen(Screen): pass
class MyListView(BoxLayout): pass
class ContainerForButtons(GridLayout):
    def __init__(self, **kwargs):
        super(ContainerForButtons, self).__init__(**kwargs)
        self.bind(minimum_height=self.setter("height"))
        self.build()
    def build(self):
        self.clear_widgets()
        self.add_some_buttons()
    def add_some_buttons(self):
        buttons_descriptions = [ chr(i) for i in range(65, 75) ]
        for item in buttons_descriptions:
            btn = Factory.CustomButtonClass()
            btn.description_a = item
            btn.description_b = "some other thing"
            btn.bind(on_press=self.execute_action_using_button_item)
            self.add_widget(btn)
        if not buttons_descriptions:
            err = "Inform user that there are no descriptions."
            self.add_widget(Label(text=err))
    @staticmethod
    def execute_action_using_button_item(*args):
        popup = Popup(title="Button callback",
                      content=Label(text="".join(map(repr, args))))
        popup.open()
        Clock.schedule_once(popup.dismiss, 1)


class kivy_test(App):
    screen_mgr = None
    @staticmethod
    def swap_screen():
        app.screen_mgr.current = app.screen_mgr.next()
    def build(self):
        Builder.load_string(textwrap.dedent(
        '''
            <CustomButtonClass@Button>:
                description_a: ''
                description_b: ''
                text: root.description_a + ' <newline> ' + root.description_b
                halign:'center'
                size_hint:(1, 0.1)
            <MyListView>:
                size_hint:(0.5, 0.5)
                ListView:
                    item_strings: [str(index) for index in range(10)]
            <OtherNamedScreen>:
                GridLayout:
                    cols: 2
                    MyListView
                    ScrollView:
                        ContainerForButtons:
                            cols:1
                            row_default_height:150
                            size_hint_y: None
        '''))
        Window.bind(on_keyboard=self.check_what_key_was_pressed)
        self.screen_mgr = ScreenManager()
        first = Screen(name='First')
        self.screen_mgr.add_widget(first)
        first.add_widget(Button(text="click me", bind=self.swap_screen))
        self.screen_mgr.add_widget(OtherNamedScreen(name='Second'))
        return self.screen_mgr
    @staticmethod
    def check_what_key_was_pressed(window, key_no, *some_other_args):
        if key_no == 27:
            app.swap_screen()
        return True

if __name__ == '__main__':
    app = kivy_test()
    app.run()

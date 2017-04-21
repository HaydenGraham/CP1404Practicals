from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty

class DynamicWidgetsApp(App):
    status_text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.phonebook = ["one","two","three"]

    def build(self):
        self.title = "Display List"
        self.root = Builder.load_file('loop_list_of_string.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in self.phonebook:

            temp_label = Button(text=name)
            self.root.ids.entriesBox.add_widget(temp_label)

DynamicWidgetsApp().run()

from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root
    def handle_greet(self):
        print("Hello {}".format(self.root.ids.input_name.text))
        self.root.ids.output_label.text = "Hello"
    def handle_clear(self):
        #\self.root.ids.btn_clr.text = "Hello"



BoxLayoutDemo().run()

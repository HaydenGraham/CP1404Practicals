from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window



class mile_to_km(App):
    """ SquareNumberApp is a Kivy App for squaring a number """
    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (200, 100)
        self.title = "Square Number"
        self.root = Builder.load_file('mile_to_km.kv')
        return self.root
    def addone(self, value):
        result = value + 1
        self.root.ids.input_number.text = str(result)
    def takeone(self, value):
        result = value - 1
        self.root.ids.input_number.text = str(result)
    def handle_calculate(self, value):
        print(value/1.6)
        result = value/1.6
        self.root.ids.output_label.text = str(result)

mile_to_km().run()

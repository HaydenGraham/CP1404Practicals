from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window



class mile_to_km(App):
    """ SquareNumberApp is a Kivy App for squaring a number """
    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (300, 500)
        self.title = "Square Number"
        self.root = Builder.load_file('mile_to_km.kv')
        return self.root
    def addone(self, value):
        result = value + 1
        self.root.ids.input_number.text = str(result)
    def takeone(self, value):
        try:
            result = value - 1

        except ValueError:
            print("thisran")
            self.root.ids.input_number.text = 0

        self.root.ids.input_number.text = str(result)
    def handle_calculate(self, value):
        try:
            print(value/1.6)
            result = value/1.6
            self.root.ids.output_label.text = str(result)
        except ValueError:
            self.root.ids.output_label.text = 0.0

mile_to_km().run()

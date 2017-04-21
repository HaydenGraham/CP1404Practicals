from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


CONVERSION = 1.6

class MilesToKilometers(App):
    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_m_km.kv')
        return self.root

    def handle_calculate(self):
        value = self.check_input()
        result = value * CONVERSION
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, change):
        value = self.check_input() + change
        self.root.ids.input_miles.text = str(value)
        self.handle_calculate()

    def check_input(self):
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0

    def changeTheme(self):
        self._digits_toggled = not self._digits_toggled

MilesToKilometers().run()
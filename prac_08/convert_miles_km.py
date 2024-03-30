from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty


class ConvertMileToKilometre(App):
    output_text = StringProperty()

    def build(self):
        Window.size = (400, 200)
        self.title = "Convert Mile to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_convert(self, miles):
        try:
            kilometres = float(miles) * 1.60934
            self.root.ids.output_label.text = str(kilometres)
        except ValueError:
            self.root.ids.output_label.text = '0.0'

    def handle_increment(self, value):
        try:
            miles = float(self.root.ids.miles.text)
            miles += value
            self.root.ids.miles.text = str(miles)
        except ValueError:
            miles = 0
            miles += value
            self.root.ids.miles.text = str(miles)


ConvertMileToKilometre().run()

from kivy.app import App
from kivy.uix.label import LabelDynamic Labels

from kivy.uix.boxlayout import BoxLayout


class DynamicLabel(App):
    def __init__(self, **kwargs):
        super(DynamicLabel, self).__init__(**kwargs)
        self.names = ["Bob Brown", "Cat Cyan", "Oren Ochre"]

    def build(self):
        main_layout = BoxLayout(orientation='vertical')
        for name in self.names:
            label = Label(text=name)
            main_layout.add_widget(label)
        return main_layout


DynamicLabel().run()

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import time


class BoxLayoutExample(BoxLayout):
    pass


'''
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        b1 = Button(text = 'Hey!')
        b2 = Button(text = 'Yo!!!')
        b3 = Button(text = 'There')
        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(b3)
        '''


class MainWidget(Widget):
    pass


class TheLabApp(App):
    pass


TheLabApp().run()

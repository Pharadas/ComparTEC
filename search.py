from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.app import runTouchApp
from kivy.uix.screenmanager import Screen

class Scroll(ScrollView):
	def __init__(self, **kwargs):
		super(Scroll, self).__init__(**kwargs)
		self.size = (Window.width, Window.height)
		layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
		layout.bind(minimum_height=layout.setter('height'))
		for i in range(100):
			btn = Button(text=str(i), size_hint_y=None, height=40)
			layout.add_widget(btn)
		self.add_widget(layout)

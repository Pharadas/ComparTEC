from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen

class Search(BoxLayout):
	def __init__(self, **kwargs):
		super(Search, self).__init__(**kwargs)
		self.size = (Window.width, Window.height)
		self.add_widget(TextInput(text='hello time'))
		self.add_widget(Button(text='Search'))

		self.orientation = 'vertical'
		layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
		layout.bind(minimum_height=layout.setter('height'))
		for i in range(20):
			btn = Button(text=str(i), size_hint_y=None, height=40)
			layout.add_widget(btn)
		root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height - 115))
		root.add_widget(layout)
		self.add_widget(root)

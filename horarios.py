from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen
import pyrebaseSetup
import random

class Horarios(BoxLayout):
	def __init__(self, **kwargs):
		super(Horarios, self).__init__(**kwargs)
		self.size = (Window.width, Window.height)
		self.add_widget(TextInput(text='Buscar'))
		self.add_widget(Button(text='Horarios'))

		self.orientation = 'vertical'
		layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
		layout.bind(minimum_height=layout.setter('height'))
		for i in range(20):
			btn = Button(text = f"{random.randint(0, 24)}:{random.randint(0, 59)}", size_hint_y=None, height=40)
			layout.add_widget(btn)
		
		root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height - 115))
		root.add_widget(layout)
		self.add_widget(root)

class Asesoria(BoxLayout):
	def __init__(self, **kwargs):
		super(Asesoria, self).__init__(**kwargs)
		self.size = (Window.width, Window.height)
		self.add_widget(TextInput(text='Buscar'))
		self.add_widget(Button(text='Asesoria'))

		self.orientation = 'vertical'
		layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
		layout.bind(minimum_height=layout.setter('height'))
		items = pyrebaseSetup.db.get()
		for person in items.each():
			if person.val()['type'] == "mae":
				btn = Button(text = f"{person.val()['user_name']}. Sala {random.randint(0, 20)}", size_hint_y=None, height=40)
				layout.add_widget(btn)
		root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height - 115))
		root.add_widget(layout)
		self.add_widget(root)
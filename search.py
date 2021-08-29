from logging import currentframe
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.anchorlayout import AnchorLayout
import pyrebaseSetup
import os, random

currentFilterString = ''

def changeScreen(instance):
	# pyrebaseSetup.currentUser = instance.text
	items = pyrebaseSetup.db.get()
	for person in items.each():
		if person.val()['user_name'] == instance.text:
			pyrebaseSetup.currentUser = person.val()
			break

	# print(pyrebaseSetup.currentUser)
	print(pyrebaseSetup.currentUser['subject'])
	path = pyrebaseSetup.currentUser['pdf_name']
	os.system('"C:/Users/david/Documents/repos/testthings/ComparTEC/testpdfs/' + path + '"')

def updateSubstringToMatch(instance):
	print(instance.text)

def on_text(instance, value):
	print('current filter string is', value)
	currentFilterString = value

class Search(BoxLayout):
	def __init__(self, **kwargs):
		self.innerSubstring = ''
		super(Search, self).__init__(**kwargs)
		currentFilterString = input('Como quieres filtrar la busqueda? ')
		self.size = (Window.width, Window.height)
		gaming = TextInput(text=currentFilterString)
		gaming.bind(text=on_text)
		self.add_widget(gaming)
		searchBtn = Button(text='Search')
		searchBtn.bind(on_press=updateSubstringToMatch)
		self.add_widget(searchBtn)

		self.orientation = 'vertical'
		layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
		layout.bind(minimum_height=layout.setter('height'))
		items = pyrebaseSetup.db.get()
		for person in items.each():
			if currentFilterString in person.val()['subject']:
				btn = Button(text = person.val()['user_name'], size_hint_y=None, height=40)
				btn.bind(on_press=changeScreen)
				layout.add_widget(btn)

		root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height - 115))
		# root.add_widget(Image(source='MayI.PNG'))
		root.add_widget(layout)
		self.add_widget(root)

	def run(self):
		print('this')
		if self.innerSubstring != currentFilterString:
			self.innerSubstring = currentFilterString
			self.update()

	def update(self):
		self.remove_widget(self.root)

		self.orientation = 'vertical'
		layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
		layout.bind(minimum_height=layout.setter('height'))
		items = pyrebaseSetup.db.get()
		for person in items.each():
			if currentFilterString in person.val()['subject']:
				btn = Button(text = person.val()['user_name'], size_hint_y=None, height=40)
				btn.bind(on_press=changeScreen)
				layout.add_widget(btn)

		root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height - 115))
		# root.add_widget(Image(source='MayI.PNG'))
		root.add_widget(layout)
		self.add_widget(root)

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen

class AddNotes(BoxLayout):
    def __init__(self, **kwargs):
        super(AddNotes, self).__init__(**kwargs)
        self.size = (Window.width, Window.height)
        self.add_widget(TextInput(text='Carga'))
        self.add_widget(Button(text='Carga'))

        self.orientation = 'vertical'
        layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))
        btn = Button(text='Añadir notas', size_hint_y=None, height=40)
        layout.add_widget(btn)
        root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height - 115))
        root.add_widget(layout)
        self.add_widget(root)
class Info(BoxLayout):
    def  __init__(self, **kwargs):
        super(Info, self).__init__(**kwargs)
        self.size = (Window.width, Window.height)
        self.add_widget(TextInput(text='Mi perfil'))
        self.add_widget(Button(text='Informacion'))

        self.orientation = 'vertical'
        layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))
        btn = Button(text='Nombre', size_hint_y=None, height=40)
        layout.add_widget(btn)
        btn = Button(text='Matricula', size_hint_y=None, height=40)
        layout.add_widget(btn)
        root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height - 115))
        root.add_widget(layout)
        self.add_widget(root)
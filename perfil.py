# kivy imports
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

# screens imports 
from notas import AddNotes

Builder.load_string("""
<PerfilScreen>:
    BoxLayout:
        orientation: 'vertical'
        Button:
            text: 'Inicio'
            size_hint: (1.0, 0.2)
            on_press: root.manager.current = 'main'
        Button:
            text: 'Añade tus notas'
            size_hint: (1.0,0.2)
            on_press: root.manager.current = 'addnotes'
        Button:
            text: 'Informacion personal'
            size_hint: (1.0,0.2)
            on_press: root.manager.current = 'info'
<AddNotesScreen>:
    AddNotes:
        size_hint: (1, None)
        Button: 
            text: 'Back'
            on_press: root.manager.current = 'perfil'
<InfoScreen>:
    Info:
        size_hint: (1, None)
        Button:
            text: 'Back'
            on_press: root.manager.current = 'perfil'
""")

# Declare both screens
class PerfilScreen(Screen):
    pass

class AddNotesScreen(Screen):
    pass
class InfoScreen(Screen):
    pass

class TestApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(PerfilScreen(name='perfil'))
        sm.add_widget(AddNotesScreen(name='addnotes'))
        sm.add_widget(InfoScreen(name='info'))

# sm.add_widget(Search(name='search'))

        return sm

if __name__ == '__main__':
    TestApp().run()
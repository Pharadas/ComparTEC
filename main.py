# kivy imports
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.widget import Widget
from horarios import Horarios
from horarios import Asesoria

# custom imports
import pyrebaseSetup

# screens imports
from search import Search

Builder.load_string("""
<MenuScreen>:
    BoxLayout:
		orientation: 'vertical'
		Button:
			text: 'Inicio'
			size_hint: (1.0, 0.2)
        Button:
            text: 'Notas'
            on_press: root.manager.current = 'search'
        Button:
            text: 'Maes'
            on_press: root.manager.current = 'asesorias'

<SearchScreen>:
    Search:
		size_hint: (1, None)
		Button:
			text: 'Back'
            on_press: root.manager.current = 'menu'

<AsesoriasScreen>:
    BoxLayout:
        orientation: 'vertical'
        Button:
            text: 'Inicio'
            size_hint: (1.0, 0.2)
            on_press: root.manager.current = 'menu'
        Button:
            text: 'Consulta horarios'
            on_press: root.manager.current = 'horarios'
        Button:
            text: 'Registra asesoria'
            on_press: root.manager.current= 'asesoria'

<HorariosScreen>:
    Horarios:
        size_hint: (1, None)
        Button:
            text: 'Back'
            on_press: root.manager.current = 'asesorias'

<AsesoriaScreen>:
    Asesoria:
        size_hint: (1, None)
        Button:
            text: 'Back'
            on_press: root.manager.current = 'asesorias'
""")

# Declare both screens
class MenuScreen(Screen):
    pass

class SearchScreen(Screen):
    pass

class AsesoriasScreen(Screen):
    pass

class HorariosScreen(Screen):
    pass

class AsesoriaScreen(Screen):
    pass

class TestApp(App):
	def build(self):
		sm = ScreenManager()
		sm.add_widget(MenuScreen(name='menu'))
		sm.add_widget(SearchScreen(name='search'))
		sm.add_widget(AsesoriasScreen(name='asesorias'))
		sm.add_widget(HorariosScreen(name='horarios'))
		sm.add_widget(AsesoriaScreen(name='asesoria'))

		return sm


if __name__ == '__main__':
	pyrebaseSetup.init()
	TestApp().run()

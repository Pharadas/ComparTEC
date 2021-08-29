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
from search import Scroll

Builder.load_string("""
<MenuScreen>:
    BoxLayout:
		orientation: 'vertical'
        Button:
            text: 'Notas'
            on_press: root.manager.current = 'search'
        Button:
            text: 'Maes'

<SearchScreen>:
    Scroll:
		size_hint: (1, None)
""")

# Declare both screens
class MenuScreen(Screen):
    pass

class SearchScreen(Screen):
    pass

class TestApp(App):
	def build(self):
		sm = ScreenManager()
		sm.add_widget(MenuScreen(name='menu'))
		sm.add_widget(SearchScreen(name='search'))
		# sm.add_widget(Search(name='search'))

		return sm

if __name__ == '__main__':
    TestApp().run()
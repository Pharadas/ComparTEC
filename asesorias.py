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
from horarios import Horarios

Builder.load_string("""
<AsesoriasScreen>:
    BoxLayout:
        orientation: 'vertical'
        Button:
            text: 'Inicio'
            size_hint: (1.0, 0.2)
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
            on_press: root.manager.current = 'menu'

<AsesoriaScreen>:
    Asesoria:
        size_hint: (1, None)
        Button:
            text: 'Back'
            on_press: root.manager.current = 'menu'
""")

# Declare both screens
class AsesoriasScreen(Screen):
    pass

class HorariosScreen(Screen):
    pass
class AsesoriaScreen(Screen):
    pass

class TestApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(AsesoriasScreen(name='asesorias'))
        sm.add_widget(HorariosScreen(name='horarios'))
        sm.add_widget(AsesoriaScreen(name='asesoria'))

# sm.add_widget(Search(name='search'))

        return sm

if __name__ == '__main__':
    TestApp().run()
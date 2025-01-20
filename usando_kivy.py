#LINGUAGEM KIVY

from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout

class Incrementador(BoxLayout):
    pass

class Usando_kivy(App):
    def build(self): 
        return Incrementador()
 
Usando_kivy().run()
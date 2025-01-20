##LAYOUTS DINÂMICOS E KWARG

from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
#from kivy.uix.button import Button

class Tarefas(BoxLayout):
    #__init__ -> inicializar dinamicamente
    #para saber o número de tarefas ao inicializar
    
    def __init__(self, tarefas, **kwargs):
        super().__init__(**kwargs)
        for tarefa in tarefas:
            self.add_widget(Label(text=tarefa, font_size=20))


class TarefasInterDinam(App):
    def build(self): 
        return Tarefas(['fazer compras', 'buscar filhos'])
    
 
TarefasInterDinam().run()
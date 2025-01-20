#SCROLL VIEW E SIZE HINTS

from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
#from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView

class Tarefas(ScrollView):
    #__init__ -> inicializar dinamicamente
    #para saber o número de tarefas ao inicializar
    
    def __init__(self, tarefas, **kwargs):
        super().__init__(**kwargs)
        for tarefa in tarefas:
            self.ids.box.add_widget(Label(text=tarefa, font_size=20, size_hint_y=None, height=100))


class Tarefasdinamic(App):
    def build(self): 
        return Tarefas(['fazer compras', 'buscar filhos', 'Comprar arroz', 'Comprar livro', 'Compras', 'Compras na feira', 'Compras', 'Compras'])
 
Tarefasdinamic().run()
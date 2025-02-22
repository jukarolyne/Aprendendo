#REFERÊNCIAS E REMOÇÃO DE WIDGETS DINAMICAMENTE

from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
#from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView

class Tarefas(ScrollView):
    def __init__(self, tarefas, **kwargs):
        super().__init__(**kwargs)
        for tarefa in tarefas:
            self.ids.box.add_widget(Tarefa(text=tarefa))

class Tarefa(BoxLayout):
   def __init__(self, text='',**kwargs):
       super().__init__(**kwargs)
       self.ids.label.text = text

class remocao(App):
    def build(self): 
        return Tarefas(['fazer compras', 'buscar filhos', 'Comprar arroz', 'Comprar livro', 'Compras', 'Compras na feira', 'Compras', 'Compras'])
 
remocao().run()
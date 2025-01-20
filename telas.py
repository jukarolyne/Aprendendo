#MÚLTIPLAS TELAS COM SCREENMANAGER
from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen

class Gerenciador(ScreenManager):
    pass

class Tarefas(Screen):
    def __init__(self, tarefas=[], **kwargs):
        super().__init__(**kwargs)
        for tarefa in tarefas:
            self.ids.box.add_widget(Tarefa(text=tarefa))
    
    def addWidget(self):
        texto = self.ids.texto.text
        self.ids.box.add_widget(Tarefa (text = texto))
        self.ids.texto.text= ''

class Tarefa(BoxLayout):
   def __init__(self, text='',**kwargs):
       super().__init__(**kwargs)
       self.ids.label.text = text

class telas(App):
    def build(self): 
        return Gerenciador()
 
telas().run()
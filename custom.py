#CLASSES DINÂMICAS E CUSTOMIZAÇÃO

from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window

class Gerenciador(ScreenManager):
    pass

class Menu(Screen):
    pass

class Tarefas(Screen):
    #**kwargs -> dicionário de parâmetros
    def __init__(self, tarefas=[], **kwargs):
        super(Tarefas, self).__init__(**kwargs)
        for tarefa in tarefas:
            self.ids.box.add_widget(Tarefa(text=tarefa))
    
    def on_pre_enter(self):
        Window.bind(on_keyboard=self.voltar)

    #*args -> lista de parâmetros
    def voltar(self, window, key, *args):
        if key == 27: #ao apertar a tecla esc (27)
            App.get_running_app().root.current = 'menu' #roda o app para voltar ao menu
            return True
    
    #fechar app com esc -> como se usasse o voltar do android
    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.voltar)
    
    def addWidget(self):
        texto = self.ids.texto.text
        self.ids.box.add_widget(Tarefa (text = texto))
        self.ids.texto.text= ''

class Tarefa(BoxLayout):
   def __init__(self, text='',**kwargs):
       super(Tarefa, self).__init__(**kwargs)
       self.ids.label.text = text

class custom(App):
    def build(self): 
        return Gerenciador()
 
custom().run()
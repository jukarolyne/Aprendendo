#CUSTOMIZAÇÃO DE WIDGETS PELO PYTHON

from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.behaviors.button import ButtonBehavior
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.graphics import Color, Ellipse, Rectangle

class Gerenciador(ScreenManager):
    pass

class Menu(Screen):
    pass

class Botao(ButtonBehavior,Label):
    def __init__(self, **kwargs):
        super(Botao,self).__init__(**kwargs)
        self.atualizar()

    def on_pos(self, *args):
        self.atualizar()

    def on_size(self, *args):
        self.atualizar()

    def atualizar(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(rgba=(1,0.4,0,1))
            Ellipse(
                size=(self.height, self.height),
                pos=self.pos)
            Ellipse(
                size=(self.height, self.height), 
                pos=(self.x+self.width-self.height,self.y))
            Rectangle(
                size=(self.width-self.height, self.height), 
                pos= (self.x+self.height/2.0, self.y))

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

class custompy(App):
    def build(self): 
        return Gerenciador()
 
custompy().run()
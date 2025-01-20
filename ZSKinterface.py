#CRIANDO A 1º INTERFACE GRÁFICA

from kivy.app import App
from kivy.uix.button import Button

class Interface(App):
    #metodo build inicializa a constrói o app
    # onde coloca o botão
    # tudo o que essa função retorna é construído na janela do app
    def build(self): 
        return Button(text='Olá Mundo!')
    
#instancia a classe e usa o método run() -> herdado de App 
Interface().run()
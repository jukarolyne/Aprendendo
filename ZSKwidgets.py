#ASSOCIANDO WIDGETS

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

#BoxLayout empilha os Widgets como se fossem caixas

class Interface(App):
    def build(self): 
        #cria um objeto (box) da classe boxlayout
        box = BoxLayout(
            orientation= 'vertical')

        label = Label(text='Label 1')
        #cria um botão
        btn = Button(text='Botão 1')
        #adiciona o widget botão no box
        #obs = a ordem que adiciona os widgets altera a ordem de visualização
        box.add_widget(label)
        box.add_widget(btn)
        box.add_widget(box)

        box2 = BoxLayout(orientation= 'vertical')
        label2 = Label(text='label 2')
        btn2 = Button(text='botão 2')
        box2.add_widget(label2)
        box2.add_widget(btn2)
        box.add_widget(box2)

        return box #retorna o layout
#instancia a classe e usa o método run() -> herdado de App 
Interface().run()
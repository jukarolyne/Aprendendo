#EVENTOS VARIÁVEIS DA INSTÂNCIA

from kivy.app import App 
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class Interface(App):
    def build(self): 
        #cria um objeto (box) da classe boxlayout
        box = BoxLayout(
            orientation= 'vertical')
        
        #ao adicionar self. => consegue acessar em outra função pela variável da classe
        #se não adiciona, não é possível acessar pois é como se fosse uma variável local
        self.label = Label(
            text='1', 
            font_size=30)

        #ao acionar o on_release, a função incrementar é usada
        btn = Button(
            text='Botão 1', 
            font_size=30,
            on_release=self.incrementar)
        box.add_widget(self.label)
        box.add_widget(btn)
        return box

    # o argumento passado é btn pois é ele que será modificado
    def incrementar(self, btn):
        btn.text = 'soltei'

        #consigo acessar a variável por conta do self.
        #muda label de acordo com a quantidade de vezes que pressiona o botão, incrementando no valor inicial 1
        self.label.text = str(int(self.label.text)+1)
 

Interface().run()
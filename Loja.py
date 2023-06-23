from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window


class Tela(BoxLayout):

    def __init__(self, **Kwargs):
        super().__init__(**Kwargs)

        self.total = 0
        self.valores = {'Martelo': 180,
                        'Marreta': 400,
                        'Motocerra': 3000,
                        'Cortador de grama': 7000
                        }

    def on(self, situation, produtos):
        if self.ids.nome.focus == False:
            self.ids.welcon.text = f'[color=#F8F8FF]Seja bem vindo(a)[/color] {self.ids.nome.text}'
            self.ids.tx1.focus = True
        if situation:
            if produtos == 'Martelo':
                self.total += int(self.ids.tx1.text) * self.valores['Martelo']
            if produtos == 'Marreta':
                self.total += int(self.ids.tx2.text) * self.valores['Marreta']
            if produtos == 'Motocerra':
                self.total += int(self.ids.tx3.text) * self.valores['Motocerra']
            if produtos == 'Cortador de grama':
                self.total += int(self.ids.tx4.text) * self.valores['Cortador de grama']

    def pay(self, tip):
        if tip == 'A vista (-5%)':
            self.total -= (self.total * 5/100.0)
        elif tip == '2 vezes (+2,5%)':
            self.total += (self.total * 2.5/100.0)
        else:
            self.total += (self.total * 8/100.0)
        self.ids.total.text = f'A pagar R$ {round(self.total,2)}'

    def clean(self):
        self.total = 0
        self.ids.nome.text = ''
        self.ids.id1.active = False
        self.ids.id2.active = False
        self.ids.id3.active = False
        self.ids.id4.active = False
        self.ids.tx1.text = ''
        self.ids.tx2.text = ''
        self.ids.tx3.text = ''
        self.ids.tx4.text = ''
        self.ids.sp1.text = 'pagamento'
        self.ids.total.text = 'A pagar R$ '


class lojaApp(App):
    def build(self):
        Window.title = 'Loja'
        Window.size = (400, 500)
        return Tela()


lojaApp().run()

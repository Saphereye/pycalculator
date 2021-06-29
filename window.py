from kivy.app import App
from kivy.uix.widget import Widget
background_data = ''
foreground_data = ''
operator = ''

def convert(a):
    if a == '*':
        return 'x'
    elif a == '/':
        return '÷'
    else:
        return a
class MyGrid(Widget):

    global background_data
    global foreground_data
    global operator

    #background_data = ObjectProperty(None)
    #foreground_data = ObjectProperty(None)
    #operator = ObjectProperty(None)


    def pressed_num(self,i):
        global foreground_data,background_data,operator
        foreground_data += i
        self.foreground_data.text = foreground_data

    def pressed_operator(self,i):
        global foreground_data,background_data,operator
        operator = i
        background_data = foreground_data
        foreground_data = ''
        self.foreground_data.text = f'{background_data}{convert(operator)}{foreground_data}'

    def pressed_C(self):
        global foreground_data,background_data,operator
        foreground_data = ''
        self.foreground_data.text = foreground_data

    def pressed_sroot(self):
        global foreground_data,background_data,operator
        foreground_data = str(float(foreground_data)**0.5)
        self.foreground_data.text = f'{foreground_data}'
        background_data = foreground_data

    def pressed_squared(self):
        global foreground_data,background_data,operator
        try:
            foreground_data = str(float(foreground_data) ** 2)
            self.foreground_data.text = f'{foreground_data}'
            background_data = foreground_data
        except OverflowError:
            self.foreground_data.text = 'Overflow'

    def pressed_ans(self):
        global foreground_data,background_data,operator
        foreground_data = background_data
        self.foreground_data.text = foreground_data

    def pressed_equals(self):
        global foreground_data,background_data,operator
        try:
            foreground_data = str(eval(f'{background_data}{operator}{foreground_data}'))
            self.foreground_data.text = foreground_data
        except ZeroDivisionError:
            self.foreground_data.text = "Can't divide by zero"
        except OverflowError:
            self.foreground_data.text = 'Overflow'

    def pressed_dot(self):
        global foreground_data, background_data, operator
        foreground_data += '.'
        self.foreground_data.text = foreground_data

    def backspace(self):
        global foreground_data, background_data, operator
        foreground_data = foreground_data[:-1]
        self.foreground_data.text = foreground_data


class CalculatorApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    CalculatorApp().run()

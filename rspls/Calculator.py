__author__ = 'yan'


import simplegui

store = 12
operand = 2

def output():
    print ("store = ", store)
    print ("operand = ", operand)
    print ("")

def swap():
    global store, operand
    store, operand = operand, store
    output()

def add():
    global store, operand
    store += operand
    output()

def sub():
    global store, operand
    store -= operand
    output()

def mul():
    global store, operand
    store *= operand
    output()

def div():
    global store, operand
    store /= operand
    output()

def input(inputText):
    global operand
    operand = float(inputText)
    output()

frame=simplegui.create_frame("Testing",200,200)
addButton = frame.add_button("Add",add,100)
subButton = frame.add_button("Sub",sub,100)
swapButton = frame.add_button("Swap",swap,100)
printButton = frame.add_button("Print",output,100)
mulButton = frame.add_button("Mul",mul,100)
divButton = frame.add_button("Div",div,100)
enter = frame.add_input("Input Operand:",input,100)

frame.start()


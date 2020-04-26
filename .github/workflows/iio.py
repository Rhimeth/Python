from tkinter import *
class MyWindow:
    def __init__(self, win):
        self.lbl1=Label(win, text='Operand 1:')
        self.lbl2=Label(win, text='Operand 2:')
        self.lbl3=Label(win, text='Result:')
        
        self.t1=Entry(bd=3)
        self.t2=Entry()
        self.t3=Entry()
        
        self.btn1 = Button(win, text = '+')
        self.btn2 = Button(win, text = '-')
        self.btn3 = Button(win, text = '*')
        self.btn4 = Button(win, text = '/')
        
        self.lbl1.place(x=10, y=50)
        self.t1.place(x=100, y=50)
        self.lbl2.place(x=10, y=100)
        self.t2.place(x=100, y=100)
        
        self.b1=Button(win, text='+', command = self.add)
        self.b2=Button(win, text='-', command = self.sub)
        self.b3=Button(win, text='*', command = self.mul)
        self.b4=Button(win, text='/', command = self.div)
        self.b2.bind('<Button-1>', self.sub)
        self.b3.bind('<Button-1>', self.mul)
        self.b4.bind('<Button-1>', self.div)
        self.b1.place(x=50, y=150)
        self.b2.place(x=100, y=150)
        self.b3.place(x=200, y=150)
        self.b4.place(x=300, y=150)
        self.lbl3.place(x=10, y=200)
        self.t3.place(x=100, y=200)
    def add(self):
        self.t3.delete(0, 'end')
        num1=int(self.t1.get())
        num2=int(self.t2.get())
        result=num1+num2
        self.t3.insert(END, str(result))
        
    def sub(self, event):
        self.t3.delete(0, 'end')
        num1=int(self.t1.get())
        num2=int(self.t2.get())
        result=num1-num2
        self.t3.insert(END, str(result))

    def mul(self, event):
        self.t3.delete(0, 'end')
        num1=int(self.t1.get())
        num2=int(self.t2.get())
        result=num1*num2
        self.t3.insert(END, str(result))

    def div(self):
        self.t3.delete(0, 'end')
        num1=int(self.t1.get())
        num2=int(self.t2.get())
        result=num1/num2
        ZeroDivisionError
        self.t3.insert(END, str(result))


window=Tk()
mywin=MyWindow(window)
window.title('Hello Python')
window.geometry("400x300+10+10")
window.mainloop()

from tkinter import *

root = Tk()
root.title("Basic Calculator")

entry1 = Entry(root)

entry2 = Entry(root)

entry3 = Entry(root)

    
myLabel1 = Label(root, text = "Operand 1:")

myLabel2 = Label(root, text = "Operand 2:")

myLabel3 = Label(root, text = "Result:")


myLabel1.grid(row = 0, column = 0)
myLabel2.grid(row = 1, column = 0)
myLabel3.grid(row = 2, column = 0)

e = Entry(root, width = 10)
e.grid(row = 0, column = 2)
e = Entry(root, width = 10)
e.grid(row = 1, column = 2)
e = Entry(root, width = 10)
e.grid(row = 2, column = 2)

def click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current)+str(number))

def add(self):
        self.t3.delete(0, 'end')
        num1=int(self.t1.get())
        num2=int(self.t2.get())
        result=num1+num2
    

      
buttonAdd = Button(text='+', padx = 20, pady = 2, command=add)

def sub():  
    v1 = entry1.get()
    v2 = entry2.get()
    
    label5 = Label(root, text= float(v1)-float(v2))
    
buttonSub = Button(text = '-', padx = 20, pady = 2, command = sub)

def mul():  
    v1 = entry1.get()
    v2 = entry2.get()

    label6 = Label(root, text =(float(v1)*float(v2)))

buttonMul = Button(text = '*', padx = 20, pady = 2, command = mul)

def div():  
    v1 = entry1.get()
    v2 = entry2.get()
    
    label7 = Label(root, text =(float(v1)/float(v2)))
   
buttonDiv = Button(text = '/', padx = 20, pady = 2, command = div)



buttonAdd.grid(row = 3, column = 0)
buttonSub.grid(row = 3, column = 2)
buttonMul.grid(row = 3, column = 4)
buttonDiv.grid(row = 3, column = 6)


root.mainloop()

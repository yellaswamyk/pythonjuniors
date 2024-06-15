from tkinter import *     
top = Tk()  
top.mainloop()    
from tkinter import *   
  
top = Tk()  
  
top.geometry("200x100")  
  
b = Button(top,text = "Simple")  
  
b.pack()  
  
top.mainaloop() 
from tkinter import *   
  
top = Tk()  
  
top.geometry("200x100")  
  
def fun():  
     messagebox.showinfo("Hello", "Red Button clicked")  
  
  
b1 = Button(top,text = "Red",command = fun,activeforeground = "red",activebackground = "pink",pady=10)  
  
from tkinter import * #sudo apt-get install python3-tk
from tkinter.ttk import Combobox
from tkinter.ttk import Checkbutton
from tkinter.ttk import Radiobutton
from tkinter import messagebox
from tkinter import Menu
from tkinter import ttk

def clicked():
    messagebox.showinfo('Заголовок', 'Текст')  
    res = "Привет {}".format(txt.get())
    lbl.configure(text=res)

window = Tk()  
combo = Combobox(window)
# chk = Checkbutton(window, text='Выбрать')
# rad1 = Radiobutton(window,text='Первый', value=1)

window.geometry('400x250')
window.title("Добро пожаловать в приложение PythonRu")  

menu = Menu(window)  
new_item = Menu(menu)  
new_item.add_command(label='Новый')  
new_item.add_separator()  
new_item.add_command(label='Изменить')
menu.add_cascade(label='Файл', menu=new_item)  
window.config(menu=menu)  

tab_control = ttk.Notebook(window)  
tab1 = ttk.Frame(tab_control)  
tab2 = ttk.Frame(tab_control)  
tab_control.add(tab1, text='Первая')  
tab_control.add(tab2, text='Вторая')  
lbl1 = Label(tab1, text='Вкладка 1')  
lbl1.grid(column=0, row=0)  
lbl2 = Label(tab2, text='Вкладка 2')  
lbl2.grid(column=0, row=0)  
tab_control.pack(expand=1, fill='both')  


btn = Button(tab2, text="Не нажимать!", bg="black", fg="red", command=clicked)
btn.grid(column=1, row=0)

lbl = Label(tab2, text="Привет", font=("Arial Bold", 20))  
lbl.grid(column=0, row=0)

txt = Entry(tab2, width=10)
# txt = Entry(window, width=10)
# txt = Entry(window,width=10, state='disabled')
txt.grid(column=0, row=1) 
txt.focus()

t1 = Text(tab1,height=5,width=20)
t1.grid(column=1,row=3)

combo = Combobox(tab1)  
combo['values'] = (1, 2, 3, 4, 5, "Текст")  
combo.current(1)  # установите вариант по умолчанию  
combo.grid(column=1, row=0)  

# chk_state = BooleanVar()  
# chk_state.set(True)  # задайте проверку состояния чекбокса  
# chk = Checkbutton(tab2, text='Выбрать', var=chk_state)  
# chk.grid(column=0, row=2)  

# rad1 = Radiobutton(tab2, text='Первый', value=1)  
# rad2 = Radiobutton(tab2, text='Второй', value=2)  
# rad3 = Radiobutton(tab2, text='Третий', value=3)  
# rad1.grid(column=0, row=3)  
# rad2.grid(column=1, row=3)  
# rad3.grid(column=2, row=3)  

window.mainloop()


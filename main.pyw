import csv
import ttkbootstrap as tb
from pathlib import Path
from tkinter import messagebox


global amount
amount = 4


def add_field_function():
    try:
        if add_field_entry != '':
            global amount
            amount += 1
            print(amount)
            name = add_field_entry.get()
            new_label = tb.Label(frame, text=f'{name}')
            new_label.grid(column=0, row=amount)
            new_entry = tb.Entry(frame)
            new_entry.grid(column=1, row=amount)
        else:
            status_label.configure(text='Ingrese un texto valido')
    except:
        status_label.configure(text='Error, intente devuelta')


def search_data():
    pass

def save_data():
    with open("./csvs/data.csv", "a", newline='') as f:
        csv.writer(f).writerow([dni_entry.get(), surname_entry.get(), name_entry.get()])

def delete_data():
    messagebox.askyesno('Confirmacion', 'Esta seguro que quiere eliminar esta entrada?')

window = tb.Window(themename="cerculean", title='App Pintos [WIP]')

frame = tb.LabelFrame(window, text='Datos de alumnos', padding=10)
frame.pack(side='left', padx=10, pady=5)

status_label = tb.Label(frame, text='')
status_label.grid(column=0, row=0)

add_field = tb.Button(frame, text='Agregar campo', bootstyle='success', command=add_field_function)
add_field.grid(column=0, row=1)
dni_label = tb.Label(frame,text='DNI')
dni_label.grid(column=0,row=2)
surname_label = tb.Label(frame,text='Apellido')
surname_label.grid(column=0,row=3)
name_label = tb.Label(frame,text='Nombre')
name_label.grid(column=0,row=4)

add_field_entry = tb.Entry(frame)
add_field_entry.grid(column=1, row=1)
dni_entry = tb.Entry(frame)
dni_entry.grid(column=1, row=2)
surname_entry = tb.Entry(frame)
surname_entry.grid(column=1, row=3)
name_entry = tb.Entry(frame)
name_entry.grid(column=1, row=4)

btn_frame = tb.Frame(window, padding=10)
btn_frame.pack(side='left')

btn1 = tb.Button(btn_frame, text='Buscar', width=12, command=search_data)
btn1.pack(pady=5)
btn2 = tb.Button(btn_frame, text='Guardar', width=12, command=save_data)
btn2.pack(pady=5)
btn3 = tb.Button(btn_frame, text='Modificar', width=12)
btn3.pack(pady=5)
btn4 = tb.Button(btn_frame, text='Eliminar', width=12, command=delete_data)
btn4.pack(pady=5)


Path("./csvs").mkdir(parents=True, exist_ok=True)
with open("./csvs/data.csv", "a+", newline='') as data_file:
    csv.writer(data_file).writerow(['DNI','Apellido','Nombre'])
    data = csv.reader(data_file)
    for row in data:
        print(row)



window.mainloop()

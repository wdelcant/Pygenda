# pygenda

# Importa modulo
from tkinter import *

# crear objeto
root = Tk()

# Titulo de la ventana
root.title("Libreta de contactos") 

# Selecciona el tamaño de la ventana
root.geometry('440x500')
root.resizable(width=False, height=False)

# Configuración del icono de la ventana
root.iconbitmap('./assets/image/addressbook.ico')

# Establecer el color de fondo de la ventana en blanco.
root.configure(bg='white')

# tomar una imagen para el fondo
bg = PhotoImage(file='./assets/image/background.png')

# etiquetarlo en el fondo
label = Label(root, image=bg)

# posiciona la imagen en la ventana
label.place(x=0, y=0)

# Lista de información
datos = []

# Añadir información
def add():
    global datos
    datos.append([Name.get(),Number.get(),Email.get(),address.get(1.0, "end-1c")])
    update_book()
    # Saving the data in a text file.
    with open('datos.txt', 'w') as file:
        file.write(str(datos))

# Creando una nueva ventana.
    message = Toplevel(root)
    message.geometry("280x80")
    message.resizable(width=False, height=False)
    message.iconbitmap('./assets/image/addressbook.ico')
    message.title("Agregado")
    Label(message, text= "Añadido a tus contactos", font=('arial 12 bold')).place(x=40,y=20)

# Ver información
def view():
    Name.set(datos[int(select.curselection()[0])][0])
    Number.set(datos[int(select.curselection()[0])][1])
    Email.set(datos[int(select.curselection()[0])][2])
    address.delete(1.0,"end")
    address.insert(1.0, datos[int(select.curselection()[0])][3])

# Eliminar información
def delete():
    del datos[int(select.curselection()[0])]
    update_book()

def reset():
    Name.set('')
    Number.set('')
    Email.set('')
    address.delete(1.0,"end")

# Actualizar información
def update_book():
    select.delete(0,END)
    for n,p,e,a in datos:
        select.insert(END, n)

# Agregar botones, etiqueta, cuadro de lista
Name = StringVar()
Number = StringVar()
Email = StringVar()

frame = Frame()
frame.pack(pady=0, padx=5)

frame1 = Frame()
frame1.pack(pady=14)

frame4 = Frame()
frame4.pack()

frame2 = Frame()
frame2.pack(pady=14)

Label(frame, text = 'Nombre: ', font='arial 12 bold').pack(side=LEFT)
Entry(frame, textvariable = Name,width=40).pack()

Label(frame1, text = 'Teléfono: ', font='arial 12 bold').pack(side=LEFT)
Entry(frame1, textvariable = Number,width=40).pack()

Label(frame4, text = 'Correo:   ', font='arial 12 bold').pack(side=LEFT)
Entry(frame4, textvariable = Email,width=40).pack()

Label(frame2, text = 'Dirección: ', font='arial 12 bold').pack(side=LEFT)
address = Text(frame2,width=30,height=5)
address.pack()

# Creando los botones.
Button(root,text="Agregar",font="arial 12 bold",command=add).place(x= 140, y=210)
Button(root,text="Ver",font="arial 12 bold",command=view).place(x= 45, y=290)
Button(root,text="Borrar",font="arial 12 bold",command=delete).place(x= 45, y=330)
Button(root,text="Limpiar",font="arial 12 bold",command=reset).place(x= 230, y=210)
Button(root, text="Cerrar",font="arial 12 bold",command = root.quit).place(x=180, y=460)

# Creación de un cuadro de lista con una barra de desplazamiento.
scroll_bar = Scrollbar(root, orient=VERTICAL,width=20)
select = Listbox(root, yscrollcommand=scroll_bar.set, width=38,height=12)
scroll_bar.config (command=select.yview)
scroll_bar.place(x=370,y=260)
select.place(x=140,y=260)

# Ejecutar Tkinter
root.mainloop()
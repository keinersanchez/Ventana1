import tkinter as tk

ventana = tk.Tk()

ventana.title("mi primera ventana")

ventana.geometry("1024x960")

lnombre = tk.Label(ventana,text="Nombre:")
lnombre.grid(row=0,column=0)

cnombre = tk.Entry(ventana,width=30)
cnombre.grid(row=0,column=1)

lapellido = tk.Label(ventana,text="Apellido:")
lapellido.grid(row=1,column=0)

capellido = tk.Entry(ventana,width=30)
capellido.grid(row=1,column=1)

ledad = tk.Label(ventana,text="Edad:")
ledad.grid(row=2,column=0)

cedad = tk.Entry(ventana,width=30)
cedad.grid(row=2,column=1)

lsexo = tk.Label(ventana,text="sexo:")
lsexo.grid(row=3,column=0)

sexoS = tk.Radiobutton(ventana,text="Masculino", state="normal",variable="opcion", value=1)
sexoS.grid(row=3,column=1)

sexoS = tk.Radiobutton(ventana,text="Femenino", state="normal",variable="opcion", value=2)
sexoS.grid(row=3,column=2)

lciudad = tk.Label(ventana, text="ciudad")
lciudad.grid(row=4,column=0)

Cciudad = tk.Listbox(ventana,width=30)
elementos =["cartagena","Bogota","medellin"]
for elemento in elementos:
    Cciudad.insert(tk.END, elemento)
Cciudad.grid(row=4,column=1)

boton=tk.Button(ventana, text='registrar')
boton.grid(row=5,column=1)

ventana.mainloop()

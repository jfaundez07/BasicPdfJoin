import tkinter as tk
from tkinter import ttk
import os
import PyPDF2

def get_pdfs():                                         #obtiene la lista de pdfs en la carpeta, y los retorna en una lista
    path = os.getcwd()                                  #obtengo la ruta del directorio
    content = os.listdir(path)                          #listo los archivos del directorio
    return content

def create_pdf_list(content):                           #crea una lista con los nombres dde archivos obtenidos que sean pdf
    content_list = []
    print('todo el contenido: ')
    print(content)

    for file in content:
        spli_path = os.path.splitext(file)              #separo el nombre de los archivos
        name = spli_path[0]                             #almaceno la separacion que corresponde al nombre
        extension = spli_path[-1]                       #almaceno la separacion que corresponde a la extension
        if extension == '.pdf':                         #si la extension es pdf, lo agrego a la lista
            file_name = name + extension 
            content_list.append(file_name) 

    print('archivos que son pdf: ')
    print(content_list)
    return content_list  

def append_pdf():                                       #agrega los pdfs a una nueva lista para ser unidos

    if len(available_pdfs) == 0:
        return
        
    selected_pdf = selec_files_combobox.get()           #obtiene el pdf seleccionado en el combo box
    pdfs_toJoin.append(selected_pdf)                    #agrega el pdf seleccionado a la lista de pdfs a unir
    available_pdfs.remove(selected_pdf)                 #elimina el pdf seleccionado de la lista de pdfs disponibles
    update_selected_label(selected_pdf)                 #actualiza el label de los pdf seleccionados

    selec_files_combobox.set('')                        #limpia el combobox
    selec_files_combobox['values'] = available_pdfs     #actualiza el combobox con los pdfs disponibles

def update_selected_label(pdf_name):                   #actualiza el label de los pdf seleccionados
    position = pdf_list_ListBox.size()
    pdf_list_ListBox.insert(position, pdf_name)

def create_pdf():                                      #crea el pdf resultante agregando los que vienen en la lista
    final_pdf_file = PyPDF2.PdfMerger()
    for pdf in pdfs_toJoin:
        final_pdf_file.append(pdf)
    name = f"{output_name_entry.get()}.pdf"
    final_pdf_file.write(name)
    final_pdf_file.close()

#----------------------------------------------------------------------------

content_inDirectory = get_pdfs()
available_pdfs = create_pdf_list(content_inDirectory)
pdfs_toJoin = []

#----------------------------------------------------------------------------

window = tk.Tk()
window.title("PDF joiner")
window.geometry("600x400")
window.configure(bg="#9BB1FF")

#----------------------------------------------------------------------------

output_name_label = tk.Label(window, text = 'Nombre del nuevo PDF:  ', bg = "#9BB1FF") #label para el nombre del pdf resultante
output_name_label.place(x=0, y=0)

output_name_entry = tk.Entry(window, width=30) #entry para el nombre del pdf resultante
output_name_entry.place(x=200, y=0)

#----------------------------------------------------------------------------

selecc_files_label = tk.Label(window, text='Selecciona los PDF para unir:  ', bg = "#9BB1FF", ) #label para la seleccion de los pdf
selecc_files_label.place(x=0, y=30)

selec_files_combobox = ttk.Combobox(window, width=30, values=available_pdfs) #combobox para seleccionar los pdf
selec_files_combobox.place(x=200, y=30)

add_button = tk.Button(window, text = 'Agregar', command=append_pdf) #boton para agregar los pdf
add_button.place(x=480, y=30)

#----------------------------------------------------------------------------

pdf_list_label = tk.Label(window, text='PDFs seleccionados:  ', bg = "#9BB1FF") #label para los pdf seleccionados
pdf_list_label.place(x=0, y=60)

pdf_list_ListBox = tk.Listbox(window, width=30) #listbox para los pdf seleccionados
pdf_list_ListBox.place(x=200, y=60)

#----------------------------------------------------------------------------

generate_button = tk.Button(window, text = 'Generar PDF', command = create_pdf) #boton para generar el pdf
generate_button.place(x=10, y=300)

#----------------------------------------------------------------------------

window.mainloop()



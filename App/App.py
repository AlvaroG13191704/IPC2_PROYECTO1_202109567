

import tkinter as tk
from tkinter.filedialog import askopenfile
from tkinter.font import BOLD

from functions.read_xml import read_xml


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        #Title
        self.title('PROYECTO 1 - APLICACIÓN DE SALUD')
        #Dimensions 
        self.geometry('600x400+700+200')
        self['background']='#dbdbdb'
        #Grid
        self.columnconfigure(0,weight=1)
        #Variables 

        self._create_components()
    
    def _create_components(self):
        #usando el sticky N(arriba), E(derecha), S(abajo), W(izquierda) 
        #Labels
        tk.Label(self,text='Laboratorio de Investigación Epidemiológica de Guatemala',font=("Verdana",14)).grid(row=0,column=0,sticky='WE',padx=10,pady=10)
        tk.Label(self,text='Cargue un archivo para continuar',font=("Verdana",14)).grid(row=1,column=0,sticky='WE',padx=10,pady=10)

        #file upload
        btn_upload = tk.Button(self,text='Cargar Archivo',command=self._file_upload,height=2,width=15)
        btn_upload.grid(row=2,column=0,pady=10)
        #file upload
        btn_upload = tk.Button(self,text='Analizar Paciente',height=2,width=15)
        btn_upload.grid(row=3,column=0,pady=10)
        #quit
        btn_quit = tk.Button(self,text='Salir',command=lambda: self.quit(),height=2,width=15)
        btn_quit.grid(row=4,column=0,pady=10)
        
    #First button command -> File Upload
    def _file_upload(self):
        # We open the file
        open_file = askopenfile(mode='r+')
        read_xml(open_file)


if __name__ == '__main__':
    main_page = App()
    main_page.mainloop()
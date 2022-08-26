# Imports

from colorama import Fore
import xml.etree.ElementTree as ET
from classes.Cell import Cell
from classes.Patient import Patient
from classes.List import List_for_cells
from components.select_and_execute_patient import select_patient

#Global variables
list_of_patients = []

def show_menu(options):
    print(Fore.CYAN + 'Bienvenidos al laboratorio de investigación epidemiológica de Guatemala')
    print(Fore.CYAN + '------------------------------------------------------------------------')
    print(Fore.CYAN + 'Seleccione una opcion: ')
    for key in sorted(options):
        print(Fore.CYAN + f'{key}) {options[key][0]}')

def read_options(options):
    while (a:= input(Fore.YELLOW + 'Opción: ')) not in options:
        print(Fore.YELLOW + 'Opción incorrecta, vuelva a intentarlo.')
    return a

def execute_option(option,options):
    options[option][1]()

def generate_menu(options,exit_option):
    option = None
    while option != exit_option:
        show_menu(options)
        option = read_options(options)
        execute_option(option,options)
        print()

def main_menu():
    options = {
        '1':('Cargar un archivo',upload_file),
        '2':('Ver pacientes',lambda: select_patient(list_of_patients)),
        '3':('Salir',exit),
    }
    generate_menu(options,'3')

#read XML
def upload_file():
    tree = ET.parse('entrada.xml')
    patients = tree.getroot()
    #print each patient
    for patient in patients:
        #print(f'Paciente')
        for personal_data in patient.iter('datospersonales'):
            #Print personal_data
            name = personal_data.find("nombre").text
            age = personal_data.find("edad").text

        #Print periods and m of the matrix
        period = patient.find("periodos").text
        m =  int(patient.find("m").text)
        
        # Create the patient object
        patient_obj = Patient(name,age,period,m)
        patient_obj.name = name
        patient_obj.age = int(age)
        patient_obj.period = int(period)
        patient_obj.matrix = m
        #print(f'Nombre: {patient_obj.name} \nedad: {patient_obj.age} Periodos: {patient_obj.period} Matrix: {patient_obj.matrix}')
        #find the cells
        infected_cells = []
        for rack in patient.iter('rejilla'):
            for cell in rack:
                cell_infected = Cell(int(cell.attrib["f"]),int(cell.attrib["c"]),True,1)
                infected_cells.append(cell_infected)

        #Create the matrix
        patient_obj.matrix_of_cells = List_for_cells()
        patient_obj.matrix_of_cells.create_matrix(m*m)
        #Add the infected cells and the ones who are not infected 
        for i in range(m):
            for j in range(m):
                for n in infected_cells:
                    if i == n.x and j == n.y:
                        patient_obj.matrix_of_cells.edit_pos(n,i,j,m)
                    elif patient_obj.matrix_of_cells.get_pos(i,j,m) == None:
                        cell = Cell(i,j,False,0)
                        patient_obj.matrix_of_cells.edit_pos(cell,i,j,m)

        #append the patient to the global navite list
        global list_of_patients
        list_of_patients.append(patient_obj)
        

    print('Se ha leido y guardado los pacientes exitosamente')
    print('-----------------------------------------------------------')

def exit():
    print('Gracías por usar nuestra aplicación ')

if __name__ == '__main__':
    main_menu()

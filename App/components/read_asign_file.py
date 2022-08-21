from colorama import Fore
import xml.etree.ElementTree as ET


def upload_file():
    tree = ET.parse('entrada.xml')
    patients = tree.getroot()

    #print each patient
    for patient in patients:
        print('-----------------------------------------------------------')
        print(f'Paciente')
        for personal_data in patient.iter('datospersonales'):
            #Print personal_data
            print(f'Nombre -> {personal_data.find("nombre").text}\nEdad -> {personal_data.find("edad").text}')

        #Print periods and m of the matrix
        print(f'periodos -> {patient.find("periodos").text} ')
        print(f'tamaño matriz -> {patient.find("m").text}')

        #find the cells
        for rack in patient.iter('rejilla'):
            for cell in rack:
                print(f'Fila -> {cell.attrib["f"]}  Columna -> {cell.attrib["c"]}')
        print('-----------------------------------------------------------')

           


        
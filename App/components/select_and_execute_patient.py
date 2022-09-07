from os import startfile, system
import xml.etree.ElementTree as ET
from colorama import Fore
from classes.List import List_for_cells

def select_patient(list_of_patients):
    print(Fore.CYAN +'-----------------Pacientes-------------------')
    #print the patients of the that were uploaded
    dict_of_patients = {}
    for i in range(len(list_of_patients)):
        print(f' {i+1}) Nombre: {list_of_patients[i].name} Edad: {list_of_patients[i].age}')
        dict_of_patients[i+1] = list_of_patients[i]

    print(Fore.CYAN +'-----------Seleccione un paciente que desea analizar-------------')
    while True:
        print('Ingrese el número del paciente a evaluar \n"0" para regresar al menu principal')
        option = int(input())
        #Select and evaluate
        
        try:
            if option == 0:
                break
        except ValueError:
            print('Ingrese una opción valida')

        for n in range(len(list_of_patients)+1):
            try:
                if option == n:
                    patient = dict_of_patients[option]
                    print(f'Has seleccionado al paciente -> {patient.name}')
                    execute_patient(patient)
            except ValueError:
                print('Ingrese una opción valida')
                
                
#This func execute any patient
def execute_patient(patient):
    #Variables
    list_of_each_period = []
    name = patient.name
    age = patient.age
    period = patient.period
    m = patient.matrix
    c_periods = 0
    print(Fore.YELLOW + '-------------------------------------------------------')
    print(Fore.YELLOW + f'Paciente: {name}')
    print(Fore.YELLOW + f'Edad: {age}')
    print(Fore.YELLOW + '---------Datos medicos--------')
    print(Fore.YELLOW + f'Periodos a analizar: {period}')
    print(Fore.YELLOW + f'Tamaño de la cuadrilla: {m}x{m}')
    print(Fore.YELLOW + '--------------------Cuadrilla Celular----------------------------')
    #This goint to help us later
    while True:
        # Variable 
        #Generate a new list
        patient_matrix = List_for_cells()
        patient_matrix.create_matrix(m*m)
        for x in range(m):
            for y in range(m):
                patient_matrix.edit_pos(patient.matrix_of_cells.get_pos(x,y,m).getSymbol(),x,y,m)
        
        list_of_each_period.append(patient_matrix)
        #another things 
        print(f'Periodos analizados -> {c_periods}')
        print_matrix(m,patient)
        print(f'1. Para ejecutar un periodo \n2. Terminar evaluación y realizar diagnostico')
        option = int(input('Ingrese una opción: '))
        if option == 1:
            c_periods += 1
            # 0 == Not infected || 1 == Infected
            # If the cell is infected and has 2 or 3 infected neighbours, in the next period continue infected, otherwise this become fury
            # If the cell ins't infected and has 3 infected neihgbours, in the next period get infected 
            # x -> ROW  y -> COL
            """
            1  2  3      (x-1,y-1) (x-1,y) (x-1,y+1)
            4  x  5  ->  (x,y-1)    (x,y)    (x,y+1) 
            6  7  8      (x+1,y-1) (x+1,y) (x+1,y+1)    
            """
            #First for to change the first attribute
            for x in range(m):
                for y in range(m):
                    # (x,y)
                    main_cell = patient.matrix_of_cells.get_pos(x,y,m)
                    # (x-1,y-1)
                    cell_1 = patient.matrix_of_cells.get_pos(x-1,y-1,m)
                    # (x-1,y)
                    cell_2 = patient.matrix_of_cells.get_pos(x-1,y,m)
                    # (x-1,y+1)
                    cell_3 = patient.matrix_of_cells.get_pos(x-1,y+1,m)
                    # (x,y-1)
                    cell_4 = patient.matrix_of_cells.get_pos(x,y-1,m)
                    # (x,y+1)
                    cell_5 = patient.matrix_of_cells.get_pos(x,y+1,m)
                    # (x+1,y-1)
                    cell_6 = patient.matrix_of_cells.get_pos(x+1,y-1,m)
                    # (x+1,y)
                    cell_7 = patient.matrix_of_cells.get_pos(x+1,y,m)
                    # (x+1,y+1)
                    cell_8 = patient.matrix_of_cells.get_pos(x+1,y+1,m)

                    # This fun return ne number neighbours cells infected 
                    cells = [cell_1,cell_2,cell_3,cell_4,cell_5,cell_6,cell_7,cell_8]
                    num_of_infected_cells = verified(cells)

                    #If the number of cells infected is 2 o 3 the cell get infected 
                    if main_cell.getSymbol() == '▒':
                        if num_of_infected_cells == 3:
                            main_cell.post_infected = 1
                        else: 
                            main_cell.post_infected = 0
                            
                    elif main_cell.getSymbol() == '█':
                        if num_of_infected_cells == 3 or num_of_infected_cells == 2:
                            main_cell.post_infected = 1
                        else: 
                            main_cell.post_infected = 0
                    
            #In this second for, the visual changed is added 
            for x in range(m):
                for y in range(m):
                    if patient.matrix_of_cells.get_pos(x,y,m).post_infected == 1:
                        patient.matrix_of_cells.get_pos(x,y,m).infected = True
                    else:
                        patient.matrix_of_cells.get_pos(x,y,m).infected = False
            
        elif option == 2:
            # If the client select this option
            # A XLM will be create with the results 
            # An Graphviz with the last matrix that was made
            print(Fore.CYAN+'----------------------------')
            print('SE HA CREADO UN DIAGNOSTICO!')
            print(Fore.CYAN+'----------------------------')
            print_graphviz(m,patient)
            # Testing the periods to generate a diagnostic
            diagnostic(patient,list_of_each_period,m)
            break
        else:
            print('Ingrese una opción valida!')


def diagnostic(patient,list,m):
    #Variables
    list_of_diagnostic = []
    data = []
    pattern_a = 'A'
    pattern_b = 'B'
    pattern_c = 'C'
    pattern_r = 'R'
    #print(list)
    for i in range(m):
        for j in range(m):
            for matrix in range(len(list)-1):
                if list[matrix].get_pos(i,j,m) == list[matrix+1].get_pos(i,j,m):
                    data.append(pattern_a)
    
    # for i in range(len(list)):
    #     for j in range(i+1,len(list)):
    #         if list[i] == list[j]:
    #             list_of_diagnostic.append(pattern_a)
    #         else:
    #             list_of_diagnostic.append(pattern_r)
    # for matrix in range(len(list)-1):
    #     if list[matrix] ==  list[matrix+1]:
    #         list_of_diagnostic.append(pattern_a)
    #     else: 
    #         list_of_diagnostic.append(pattern_r)

    # print(list_of_diagnostic)
            
    # print(list_of_diagnostic)
    # Create a XML
    xml_response(patient)


def xml_response(patient):
    # With this func me decorate our XMl to give him a good apparience 
    def indent(elem,level=0):
        i = "\n" + level*"  "
        j = "\n" + (level-1)*"  "
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i + "  "
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
            for subelem in elem:
                indent(subelem, level+1)
            if not elem.tail or not elem.tail.strip():
                elem.tail = j
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = j
        return elem
    # Create the ELement
    patients = ET.Element('pacientes')
    person = ET.SubElement(patients,'paciente')
    # Sub element that contain the patient information
    personal_data = ET.SubElement(person,'datospersonales')
    name = ET.SubElement(personal_data,'nombre')
    age = ET.SubElement(personal_data,'edad')
    name.text = patient.name
    age.text = str(patient.age)

    period = ET.SubElement(person,'periodos')
    period.text = str(patient.period)

    matrix = ET.SubElement(person,'m')
    matrix.text = str(patient.matrix)

    result = ET.SubElement(person,'resultado')
    result.text = 'Leve'

    n = ET.SubElement(person,'n')
    n.text = '99'

    n1 = ET.SubElement(person,'n1')
    n1.text = '1'

    # EXPORT
    tree = ET.ElementTree(indent(patients))
    tree.write(f'{patient.name}_diagnostico.xml',xml_declaration=True, encoding='utf-8')

    

#This functions count the neighbours cells infected 
def verified(list):
    c = 0
    for cell in list:
        if cell is not None:
            if cell.getSymbol() == '█':
                c +=1
    return c

#This fun print any matrix
def print_matrix(m,patient):
    for i in range(m):
        for j in range(m):
            print('',f'{patient.matrix_of_cells.get_pos(i,j,m).getSymbol()}',end='')
        print('\n')


# Crear un graphviz
def print_graphviz(m,patient):
    graph = '''
digraph Patient{
    node [shape=box, nodesep=1, fillcolor=blue, style=filled]
    compound=true
    edge[fontcolor="black" color="#ff5400"]
    subgraph cluster_periodo {
        bgcolor = "#398D9C"
'''
    graph += f'''
        label = "Paciente: {patient.name} - Periodo N.{patient.period}"
    '''
    for x in range(m):
        for y in range(m):
            cell = patient.matrix_of_cells.get_pos(x,y,m)
            graph += f'''
        nodoF{str(x)}_C{str(y)}[label=" ({x},{y})", fillcolor="{cell.getColor()}"];
    '''
    # generate the ranks    
    cc = 0
    while m > cc:
        string = ''
        rank = '{rank = same'
        rank_f = '}' 
        for x in range(m):
            rank_value = f''';nodoF{str(cc)}_C{str(x)}'''
            string += rank_value
        graph += f'''
        {rank}{string}{rank_f}
        '''
        cc+=1
    # generate the unions betwewen columns
    cc_g = 0
    while m > cc_g:
        string_2 = ''
        for x in range(m):
            rank_value_2 = f'''nodoF{str(cc_g)}_C{str(x)}'''
            string_2 += f'{rank_value_2} -> '
        new_string = string_2[:-4]

        if not cc_g % 2 == 0:
            graph += f'''
        {new_string} [dir=back];
        '''
        else:
            graph += f'''
        {new_string};
        '''
        cc_g+=1
    # generate the unions betwewen rows
    string_3 = ''
    for x in range(m):
        union = f'''nodoF{str(x)}_C{str(0)} -> '''
        string_3 += union
    new_string_2 = string_3[:-4]
    graph += f'''
    {new_string_2};
    '''
    graph += '''
    }   
    '''
    graph += '''
}   
    '''
    #generate  graphviz
    # compilated
    miArchivo = open(f'graphviz.dot','w')
    miArchivo.write(graph)
    miArchivo.close()
    system(f'dot -Tpng graphviz.dot -o {patient.name}_gráfica.png')
    system(f'cd ./{patient.name}_gráfica.png')
    startfile(f'{patient.name}_gráfica.png')
    # print(graph)

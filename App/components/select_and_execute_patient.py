from colorama import Fore

def select_patient(list_of_patients):
    print(Fore.CYAN +'-----------------Pacientes-------------------')
    #print the patients of the that were uploaded
    dict_of_patients = {}
    for i in range(len(list_of_patients)):
        print(f' {i+1}) Nombre: {list_of_patients[i].name} Edad: {list_of_patients[i].age}')
        dict_of_patients[i+1] = list_of_patients[i]

    print(Fore.CYAN +'-----------Seleccione un paciente que desea analizar-------------')
    while True:
        option = int(input('Ingrese el número del paciente a evaluar: '))
        #Select and evaluate
        for n in range(len(list_of_patients)+1):
            if option == n:
                patient = dict_of_patients[option]
                print(f'Has seleccionado al paciente -> {patient.name}')
                execute_patient(patient)
                
                

#
def execute_patient(patient):
    #Variables
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
        print(f'Periodos analizados -> {c_periods}')
        print_matrix(m,patient)
        print(f'1. Para ejecutar un periodo \n2. Terminar evaluación ')
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
                    cell_5 = patient.matrix_of_cells.get_pos(x-1,y-1,m)
                    # (x+1,y-1)
                    cell_6 = patient.matrix_of_cells.get_pos(x+1,y-1,m)
                    # (x+1,y)
                    cell_7 = patient.matrix_of_cells.get_pos(x+1,y,m)
                    # (x+1,y+1)
                    cell_8 = patient.matrix_of_cells.get_pos(x+1,y+1,m)

                    # This fun return ne number neighbours cells infected 
                    cells = [cell_1,cell_2,cell_3,cell_4,cell_5,cell_6,cell_7,cell_8]
                    num_of_infected_cells = verified(cells)
                    
            # CHANGE THIS
                    # Now change their
                    if num_of_infected_cells == 2 or num_of_infected_cells == 3:
                        main_cell.post_infected = 1
                    elif num_of_infected_cells == 0:
                        main_cell.post_infected = 0
            # Second for to change to infected
            for x in range(m):
                for y in range(m):
                    cell = patient.matrix_of_cells.get_pos(x,y,m)
                    if cell.post_infected == 1:
                        cell.infected = True

        elif option == 2:
            print('Acá se crea el XML con el diagnostico, una función probablemente')
            break
        else:
            print('Ingrese una opción valida!')

    
def verified(list):
    c = 0
    for cell in list:
        if cell is not None:
            if cell.post_infected == 1:
                c +=1
    return c


#This fun print any matrix
def print_matrix(m,patient):
    for i in range(m):
        for j in range(m):
            print('',f'{patient.matrix_of_cells.get_pos(i,j,m).getSymbol()}',end='')
        print('\n')

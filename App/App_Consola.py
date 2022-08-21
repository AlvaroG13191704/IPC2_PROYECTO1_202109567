from colorama import Fore
# Main functions
from components.read_asign_file import upload_file
from components.select_and_execute_patient import select_patient


#Global variables




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
        '2':('Ver paciente',select_patient),
        '3':('Salir',exit),
    }
    generate_menu(options,'3')



def exit():
    print('Gracías por usar nuestra aplicación ')

if __name__ == '__main__':
    main_menu()
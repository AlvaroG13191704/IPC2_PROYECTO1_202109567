import xml.etree.ElementTree as ET

from xml.dom import minidom


def read_xml_2(xml_file):
    try:
        if xml_file.readable():
            print('Si se pudo leer')
            #Read data
            xml_data = ET.fromstring(xml_file.read())
            print(xml_data)
            #Read "paciente"
            list_patient = xml_data.findall('paciente')
            for patient in list_patient:
                print(f'Datos personales: {patient.findall("datospersonales").text}')
                print(f'Periodos: {patient.find("periodos").text}')
                print(f'Matriz de: {patient.find("m").text}')
                print(f'Rejillas: {patient.find("rejilla").text}')
                print('--------------------------------------------------')
        else:
            print('no se pudo leer')
    except Exception as err:
        print(f'Error : {err}')
    finally:
        xml_file.close()

#Another way 
def read_xml(xml_file):
    try:
        doc = minidom.parse(xml_file)
        if doc:
            print('si se pudo leer')
            print(doc)
        else:
            print('no se pudo leer')

    except Exception as err:
        print(f'Error: {err} ')
    finally:
        pass

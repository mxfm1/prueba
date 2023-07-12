import time

total_pisos = ['A1','A2','A3','A4','B1','B2','B3','B4','C1','C2','C3','C4','D1','D2','D3','D4']
depto_comprados = []
lista_compradores = []
pisos_depto = ['1','2','3','4']
letras_depto = ['A','B','C','D']


def menu():
    print('1. Comprar Departamento. ')
    print('2. Mostrar Departamentosdisponibles. ')
    print('3. Ver listado de compradores. ')
    print('4. Mostrar ganancias totales. ')
    print('5. Salir. ')

def validar_depto(departamento):
    disponibilidad = True
    for depto in depto_comprados:
        if depto == departamento:
            disponibilidad = False
    if disponibilidad:
        return True
    else: 
        return False
    
def calculo_precio_depto(depto):
    if depto[0] == 'A':
        depto_tipo_a +=1
        return 3800
    elif depto[0] == 'B':
        depto_tipo_b+=1
        return 3000
    elif depto[0] == 'C':
        depto_tipo_c+=1
        return 2800
    elif depto[0] == 'D':
        depto_tipo_d+=1
        return 3500

def mostrar_departamentos_disponibles():
    print('Los departamentos disponibles son \n')
    totalidad_pisos = ''
    for depto in total_pisos:
        print(depto)

def compra_departamentos():

    mostrar_departamentos_disponibles()
    while True:
        rut_cliente = input('Ingresa el rut del cliente. ')
        if not rut_cliente.isdigit():
            print('Debes ingresar numeros solamente. ')
            continue
        if len(rut_cliente) > 8 or len(rut_cliente) < 6:
            print('Error en la longitud del rut. Intenta nuevamente. ')
            continue
        piso_interesado = input('Ingresa el piso del departamento interesado en comprar. ')
        while piso_interesado not in pisos_depto:
            piso_interesado = input('Solo existen 4 pisos. Intenta nuevamente. ')
        letra_interesada = input('Ingresa el departamento que quieras comprar. ').upper()
        while letra_interesada not in letras_depto:
            letra_interesada = input('Departamento incorrecto. Intenta nuevamente. ').upper()
        depto_comprado = f'{letra_interesada}{piso_interesado}'

        print('Buscando disponibilidad....')
        time.sleep(1)
        disp = validar_depto(depto_comprado)
        if disp:
            print('Departamento disponible')
        else:
            print('Departamento ocupado. Intenta nuevamente. ')
            continue
        depto_comprados.append(depto_comprado)
        total_pisos.remove(depto_comprado)
        lista_compradores.append(rut_cliente)
        precio_depto= calculo_precio_depto(depto_comprado)

def listado_compradores():
    lista_clientes_ordenada = lista_compradores.sort()
    print(lista_clientes_ordenada)

while True:
    menu()
    try:
        op = int(input('Ingresa la opcion. '))
        if op == 1:
            compra_departamentos()
        elif op == 2:
            mostrar_departamentos_disponibles()
        elif op == 3:
            lista_compradores()
        elif op == 5:
            break
        else:
            print('Fuera de las opciones especificadas. ')
    except ValueError:
        print('Ingresa solo numeros. ')


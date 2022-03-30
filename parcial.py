#Dado S, Determinar el número de palabras en S

def conversion_case(nombre_variable):
    return ''.join(p.capitalize() for p in nombre_variable.split('_'))

    print(conversion_case('nombre_variable'))
    print(conversion_case('palabra_min'))
# SACAR CUAL ES EL PROFESOR Y CUAL ES EL ASISTENTE POR EDAD

def get_compa(cantidad):

    ## acá creamos el count, y un array vacio para agregar a los compas 
    parners = []
    count = 0

    ## Hacemos un for donde va pidiendo nombre y edad y los va agregando 
    for i in range(cantidad):
        count+= 1
        name = input(f'What is your name?? {count}: ')
        age = int(input(f'How old are you?? {count}: '))
        parne = (name,age)
        parners.append(parne)

    # Aca ordenamos las edades de menor a mayor con sort, y asignamos el asistente con la edad menor y el profesor con la edad mayor
    parners.sort(key=lambda x:x[1])
    asistente = parners[0][0]
    profesor = parners[-1][0]
    return asistente, profesor

## Aca descomponemos el asistente y profesor y mencionamos que son 5 personas 
asistente, profesor = get_compa(5)

# Imprimimos quien es el profesor y el asistente
print(f'El profesor es: {profesor} y el asistente es: {asistente}')
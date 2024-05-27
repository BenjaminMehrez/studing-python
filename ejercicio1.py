#Duracion de cada curso

curso_dalto = 1.5
curso_promedio = 4
curso_max = 7
curso_min = 2.5

#Duracion de crudos
crudo_dalto = 3.5
crudo_promedio = 5

#Diferencia de duracion 

diferencia_min = 100 - curso_dalto * 1000 / curso_min / 10
diferencia_max = 100 - curso_dalto * 1000 / curso_max / 10
diferencia_promedio = 100 - curso_dalto * 1000 / curso_promedio /10

diferencia_vacio_promedio = 100 - curso_promedio *1000 / crudo_promedio / 10
diferencia_crudo = 100 - curso_dalto *1000 / crudo_dalto / 10

print('El curso de dalto dura:')
print( f' - un {int(diferencia_min)}% menos que el mas rapido')
print( f' - un {int(diferencia_max)}% menos que el mas lento')
print( f' - un {int(diferencia_promedio)}% menos que el promedio')

print('------------------')
print(f'Un curso promedio elimima un {int(diferencia_vacio_promedio)}% de tiempo vacio')
print(f'Este curso elimino el {int(diferencia_crudo)}% de tiempo vacio')
print('------------------')
print(f'Ver 10 horas de este curso {round(curso_promedio *100// curso_dalto /10)} horas del curso mas rapido')
print(f'Ver 10 horas de este curso {round(curso_dalto *100 // curso_promedio /10)} horas del curso mas lento')



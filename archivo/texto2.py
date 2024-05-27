#ABRIENDO Y CERRANDO MAS OPTIMO 

#con w se encribe una sola vez
with open('archivo\\texto.txt', 'w') as archivo:

    archivo.write('Hola pa como andas')


#'con a se va agragando todas las veces que run'
with open('archivo\\texto2.txt','w') as archivo2:

    archivo2.writelines(['-Hola loco como andas\n', '-Yo todo bien y vos', '-Que raro vos siempre estas mal'])
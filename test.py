# ------- GENERANDO PASSWORD 
# def create_password(num):
#     chars = 'abcdefghij'
#     num_entero = str(num)
#     num = int(num_entero[0])
#     c1 = num - 2
#     c2 = num 
#     c3 = num - 5
#     password = f'{chars[c1]}{chars[c2]}{chars[c3]}{num*2}'
#     print(password)


# create_password(98)

numeros = [1,2,3,5,8,2,4,5,]

num_enteros = filter(lambda num: num%2 == 0, numeros)

print(list(num_enteros))
# SACAR NUMERO PRIMOS

def numero_primos(num):
    for i in range(2,num-1):
        if num%i==0: return False
    return True

def primos_hasta(num):
    primos = []
    for i in range(3,num+1):
        resutl = numero_primos(i)
        if resutl: primos.append(i)
    return primos


result = primos_hasta(13)
print(result)
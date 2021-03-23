#Quinto desafio

print('Ingrese dos cadenas de texto')
cadena_1 = input()
cadena_2 = input()
long_cadena_1 = len(cadena_1)
long_cadena_2 = len(cadena_2)
if (long_cadena_1 > long_cadena_2) :
    print(cadena_1)
elif (long_cadena_2 > long_cadena_1):
    print(cadena_2)
else:
    print('Ambas cadenas tienen el mismo tamanio')